import {
  Column,
  CreateDateColumn,
  Entity,
  Index,
  PrimaryGeneratedColumn,
} from 'typeorm';
import type { GameModeId } from '@oracle-game/shared';

/**
 * SDD §5.1 + §5.2: 모든 답변 이력.
 *
 * 향후 Spaced Repetition (SM-2/FSRS) 알고리즘이 이 테이블을 입력으로 사용한다.
 * 따라서 모든 솔로/대전 답변은 정답 여부와 응답 시간을 함께 기록한다.
 *
 * 인덱스:
 *  - (user_id, created_at): 사용자별 최근 답변 조회
 *  - (user_id, question_id): SR 알고리즘이 동일 문제에 대한 이력을 조회
 */
@Entity('answer_history')
@Index(['userId', 'createdAt'])
@Index(['userId', 'questionId'])
export class AnswerHistoryEntity {
  @PrimaryGeneratedColumn('uuid')
  id!: string;

  @Column({ type: 'uuid', name: 'user_id' })
  userId!: string;

  @Column({ type: 'uuid', name: 'question_id' })
  questionId!: string;

  @Column({ type: 'text' })
  answer!: string;

  @Column({ type: 'boolean', name: 'is_correct' })
  isCorrect!: boolean;

  @Column({ type: 'int', default: 0 })
  score!: number;

  @Column({ type: 'int', name: 'time_taken_ms' })
  timeTakenMs!: number;

  @Column({ type: 'int', name: 'hints_used', default: 0 })
  hintsUsed!: number;

  @Column({ type: 'varchar', length: 30, name: 'game_mode' })
  gameMode!: GameModeId;

  @CreateDateColumn({ name: 'created_at' })
  createdAt!: Date;
}
