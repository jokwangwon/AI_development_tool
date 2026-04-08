import type { Difficulty, Topic } from './curriculum';
import type { Question } from './question';

/**
 * 5가지 게임 모드 식별자
 */
export const GAME_MODE_IDS = [
  'blank-typing',
  'term-match',
  'result-predict',
  'category-sort',
  'scenario',
] as const;

export type GameModeId = (typeof GAME_MODE_IDS)[number];

export const GAME_MODE_LABELS: Record<GameModeId, string> = {
  'blank-typing': '빈칸 타이핑',
  'term-match': '용어 맞추기',
  'result-predict': '결과 예측',
  'category-sort': '카테고리 분류',
  scenario: '시나리오 시뮬레이션',
};

/**
 * 라운드 생성 설정
 */
export interface RoundConfig {
  topic: Topic;
  week: number;
  difficulty: Difficulty;
  timeLimit: number; // seconds
}

/**
 * 한 라운드 = 한 문제 + 정답 + 메타데이터
 */
export interface Round {
  id: string;
  question: Question;
  correctAnswers: string[]; // 복수 정답 허용 (대소문자 무시)
  hints: string[];
  timeLimit: number;
  config: RoundConfig;
}

/**
 * 플레이어가 제출한 답변
 */
export interface PlayerAnswer {
  roundId: string;
  playerId: string;
  answer: string;
  submittedAt: number; // epoch ms
  hintsUsed: number;
}

/**
 * 채점 결과
 */
export interface EvaluationResult {
  roundId: string;
  playerId: string;
  isCorrect: boolean;
  matchedAnswer?: string; // 어떤 정답과 매칭되었는지
  score: number;
  timeTakenMs: number;
  hintsUsed: number;
}

/**
 * 게임 모드 인터페이스 (Strategy Pattern)
 *
 * 모든 게임 모드는 이 인터페이스를 구현한다.
 * 새로운 모드 추가 시 이 인터페이스만 구현하면 된다.
 */
export interface GameMode {
  readonly id: GameModeId;
  readonly name: string;
  readonly description: string;
  readonly supportedTopics: readonly Topic[];

  /**
   * 라운드 생성: 문제 풀에서 조건에 맞는 문제를 선택하거나 AI로 생성
   */
  generateRound(question: Question, config: RoundConfig): Round;

  /**
   * 답변 채점: 정답 여부 + 점수 계산
   */
  evaluateAnswer(round: Round, answer: PlayerAnswer): EvaluationResult;
}
