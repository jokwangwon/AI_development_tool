import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { LessThanOrEqual, Repository } from 'typeorm';
import type { Difficulty, GameModeId, Topic } from '@oracle-game/shared';

import { QuestionEntity } from '../entities/question.entity';

export interface QuestionQuery {
  topic: Topic;
  week: number;
  gameMode: GameModeId;
  difficulty?: Difficulty;
}

@Injectable()
export class QuestionPoolService {
  constructor(
    @InjectRepository(QuestionEntity)
    private readonly questionRepo: Repository<QuestionEntity>,
  ) {}

  /**
   * 주어진 조건에 맞는 활성 문제를 무작위로 N개 조회한다.
   * 학습 범위 누적: 1주차 사용자도 1주차까지의 모든 문제를 풀 수 있도록
   * `week <= request.week` 로 누적 조회한다.
   */
  async pickRandom(query: QuestionQuery, count: number): Promise<QuestionEntity[]> {
    const qb = this.questionRepo
      .createQueryBuilder('q')
      .where('q.status = :status', { status: 'active' })
      .andWhere('q.topic = :topic', { topic: query.topic })
      .andWhere('q.gameMode = :gameMode', { gameMode: query.gameMode })
      .andWhere('q.week <= :week', { week: query.week });

    if (query.difficulty) {
      qb.andWhere('q.difficulty = :difficulty', { difficulty: query.difficulty });
    }

    qb.orderBy('RANDOM()').limit(count);

    return qb.getMany();
  }

  async findById(id: string): Promise<QuestionEntity> {
    const q = await this.questionRepo.findOne({ where: { id } });
    if (!q) {
      throw new NotFoundException(`Question ${id} not found`);
    }
    return q;
  }

  async countByWeek(week: number): Promise<number> {
    return this.questionRepo.count({
      where: { status: 'active', week: LessThanOrEqual(week) },
    });
  }

  async save(question: Partial<QuestionEntity>): Promise<QuestionEntity> {
    const entity = this.questionRepo.create(question);
    return this.questionRepo.save(entity);
  }
}
