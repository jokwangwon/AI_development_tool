// Jarvis MVP-0 트랙 B: Landlock fs sandboxer (no userns, no root, no container)
//
// 답습: docs/phase0/jarvis-safety-layer-poc-findings.md §6 (V-2 실증, ABI 7)
//       docs/phase0/jarvis-orchestrator-mvp-design-brief.md §6 / Q-9
//   - V-2 에서 직접 Landlock C(path_beneath)로 작업디렉터리 격리 실증 완료.
//     이 소스 = 그 검증된 PoC 코드를 트랙 B 격리 backend 로 *그대로* 재사용한다.
//   - Landlock = 이 머신(24.04 apparmor_restrict_unprivileged_userns=1)에서
//     추가 권한 0 으로 작동하는 유일 워커 격리(V-F1). 커널 강제 = 워커 침해 무관(V-F2).
//   - 검증된 격리 = fs 한정(V-F4). net egress 미차단 = MVP-1+ 후속(ABI4).
//
// Usage: ll_sandbox <allowed_rw_dir> [more_ro_dirs...] -- <cmd> [args...]
// First dir = read/write/execute allowed; remaining before "--" = read/execute only.
// Everything else on the fs is denied. Demonstrates worker-per-workdir isolation.
#define _GNU_SOURCE
#include <linux/landlock.h>
#include <sys/syscall.h>
#include <sys/prctl.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#ifndef LANDLOCK_ACCESS_FS_REFER
#define LANDLOCK_ACCESS_FS_REFER (1ULL << 13)
#endif
#ifndef LANDLOCK_ACCESS_FS_TRUNCATE
#define LANDLOCK_ACCESS_FS_TRUNCATE (1ULL << 14)
#endif

static int ll_create_ruleset(const struct landlock_ruleset_attr *attr, size_t size, __u32 flags) {
    return syscall(__NR_landlock_create_ruleset, attr, size, flags);
}
static int ll_add_rule(int fd, enum landlock_rule_type t, const void *attr, __u32 flags) {
    return syscall(__NR_landlock_add_rule, fd, t, attr, flags);
}
static int ll_restrict_self(int fd, __u32 flags) {
    return syscall(__NR_landlock_restrict_self, fd, flags);
}

#define ACCESS_FS_ROUGHLY_READ ( \
    LANDLOCK_ACCESS_FS_EXECUTE | LANDLOCK_ACCESS_FS_READ_FILE | LANDLOCK_ACCESS_FS_READ_DIR)
#define ACCESS_FS_ROUGHLY_WRITE ( \
    LANDLOCK_ACCESS_FS_WRITE_FILE | LANDLOCK_ACCESS_FS_REMOVE_DIR | \
    LANDLOCK_ACCESS_FS_REMOVE_FILE | LANDLOCK_ACCESS_FS_MAKE_CHAR | \
    LANDLOCK_ACCESS_FS_MAKE_DIR | LANDLOCK_ACCESS_FS_MAKE_REG | \
    LANDLOCK_ACCESS_FS_MAKE_SOCK | LANDLOCK_ACCESS_FS_MAKE_FIFO | \
    LANDLOCK_ACCESS_FS_MAKE_BLOCK | LANDLOCK_ACCESS_FS_MAKE_SYM | \
    LANDLOCK_ACCESS_FS_REFER | LANDLOCK_ACCESS_FS_TRUNCATE)

// 디딤돌1h CL-4: 파일/디바이스 노드 전용 access — 디렉터리 bit(READ_DIR/MAKE_*/
// REMOVE_*/REFER) 제거. 디렉터리 bit 를 파일 fd 에 적용 시 add_rule EINVAL(F3).
#define ACCESS_FS_FILE_RW ( \
    LANDLOCK_ACCESS_FS_READ_FILE | LANDLOCK_ACCESS_FS_WRITE_FILE | LANDLOCK_ACCESS_FS_EXECUTE)

static int allow_path(const char *path, int ruleset_fd, __u64 allowed) {
    // 디딤돌1h: 비-디렉터리(파일/디바이스)는 파일용 mask 로 좁힌다(EINVAL 회피).
    // 블록 디바이스(/dev/sda 등)는 명시 거부 — Python _safe_rw_device(S_ISCHR-only)에
    // 더해 C 2차 방어(ll_sandbox 직접 호출 경로 차단, 합의 CL-4).
    struct stat st;
    if (!stat(path, &st) && !S_ISDIR(st.st_mode)) {
        if (S_ISBLK(st.st_mode)) {
            fprintf(stderr, "reject block device: %s\n", path);
            return -1;
        }
        allowed &= ACCESS_FS_FILE_RW;
    }
    struct landlock_path_beneath_attr pb = {0};
    pb.parent_fd = open(path, O_PATH | O_CLOEXEC);
    if (pb.parent_fd < 0) { fprintf(stderr, "open(%s): %s\n", path, strerror(errno)); return -1; }
    pb.allowed_access = allowed;
    int rc = ll_add_rule(ruleset_fd, LANDLOCK_RULE_PATH_BENEATH, &pb, 0);
    close(pb.parent_fd);
    if (rc) { fprintf(stderr, "add_rule(%s): %s\n", path, strerror(errno)); return -1; }
    return 0;
}

int main(int argc, char **argv) {
    int sep = -1;
    for (int i = 1; i < argc; i++) if (!strcmp(argv[i], "--")) { sep = i; break; }
    if (sep < 2 || sep + 1 >= argc) {
        fprintf(stderr, "usage: %s <rw_dir> [ro_dir...] -- <cmd> [args]\n", argv[0]);
        return 2;
    }

    int abi = ll_create_ruleset(NULL, 0, LANDLOCK_CREATE_RULESET_VERSION);
    if (abi < 1) { fprintf(stderr, "Landlock unavailable (abi=%d): %s\n", abi, strerror(errno)); return 1; }
    fprintf(stderr, "[ll_sandbox] Landlock ABI = %d\n", abi);

    __u64 handled = ACCESS_FS_ROUGHLY_READ | ACCESS_FS_ROUGHLY_WRITE;
    if (abi < 2) handled &= ~LANDLOCK_ACCESS_FS_REFER;
    if (abi < 3) handled &= ~LANDLOCK_ACCESS_FS_TRUNCATE;

    struct landlock_ruleset_attr ra = {0};
    ra.handled_access_fs = handled;
    int ruleset_fd = ll_create_ruleset(&ra, sizeof(ra), 0);
    if (ruleset_fd < 0) { fprintf(stderr, "create_ruleset: %s\n", strerror(errno)); return 1; }

    // first dir = rw, remaining = ro 디렉터리 / RW 파일(디바이스). 디딤돌1h:
    // sep 전 인자가 *파일*이면 RW 파일 mask(allow_path 가 FILE_RW 로 좁힘+BLK 거부),
    // 디렉터리면 RO. claude Bash 의 /dev/null 쓰기(2>/dev/null) 복구.
    if (allow_path(argv[1], ruleset_fd, handled)) return 1;
    fprintf(stderr, "[ll_sandbox] RW allow: %s\n", argv[1]);
    for (int i = 2; i < sep; i++) {
        struct stat st;
        __u64 acc = (!stat(argv[i], &st) && !S_ISDIR(st.st_mode))
                    ? handled                                // 파일: allow_path 가 FILE_RW 마스킹
                    : (handled & ~ACCESS_FS_ROUGHLY_WRITE);  // 디렉터리: RO
        if (allow_path(argv[i], ruleset_fd, acc)) return 1;
        fprintf(stderr, "[ll_sandbox] allow: %s\n", argv[i]);
    }

    if (prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0)) { perror("prctl"); return 1; }
    if (ll_restrict_self(ruleset_fd, 0)) { perror("restrict_self"); return 1; }
    close(ruleset_fd);
    fprintf(stderr, "[ll_sandbox] restricted, exec: %s\n", argv[sep+1]);
    execvp(argv[sep+1], &argv[sep+1]);
    perror("execvp");
    return 127;
}
