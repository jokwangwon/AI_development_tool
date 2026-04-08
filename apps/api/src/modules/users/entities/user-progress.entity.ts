import {
  Column,
  Entity,
  Index,
  PrimaryGeneratedColumn,
  UpdateDateColumn,
} from 'typeorm';

@Entity('user_progress')
@Index(['userId', 'topic', 'week'], { unique: true })
export class UserProgressEntity {
  @PrimaryGeneratedColumn('uuid')
  id!: string;

  @Column({ type: 'uuid', name: 'user_id' })
  userId!: string;

  @Column({ type: 'varchar', length: 50 })
  topic!: string;

  @Column({ type: 'int' })
  week!: number;

  @Column({ type: 'int', name: 'total_score', default: 0 })
  totalScore!: number;

  @Column({ type: 'int', name: 'games_played', default: 0 })
  gamesPlayed!: number;

  @Column({ type: 'real', default: 0 })
  accuracy!: number;

  @Column({ type: 'int', default: 0 })
  streak!: number;

  @UpdateDateColumn({ name: 'last_played_at' })
  lastPlayedAt!: Date;
}
