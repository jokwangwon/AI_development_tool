import { BadRequestException, Injectable } from '@nestjs/common';
import {
  type Difficulty,
  type GameModeId,
  type PlayerAnswer,
  type Round,
  type Topic,
} from '@oracle-game/shared';

import { QuestionPoolService } from '../../content/services/question-pool.service';
import { GameModeRegistry } from '../modes/game-mode.registry';

const DEFAULT_TIME_LIMIT_BY_DIFFICULTY: Record<Difficulty, number> = {
  EASY: 20,
  MEDIUM: 15,
  HARD: 10,
};

interface StartSoloInput {
  topic: Topic;
  week: number;
  gameMode: GameModeId;
  difficulty: Difficulty;
  rounds: number;
}

@Injectable()
export class GameSessionService {
  // 활성 라운드를 메모리에 보관 (단일 인스턴스 가정).
  // 멀티 인스턴스 확장 시 Redis로 이전.
  private readonly activeRounds = new Map<string, Round>();

  constructor(
    private readonly registry: GameModeRegistry,
    private readonly pool: QuestionPoolService,
  ) {}

  async startSolo(input: StartSoloInput): Promise<Round[]> {
    if (input.rounds < 1 || input.rounds > 50) {
      throw new BadRequestException('rounds는 1~50 사이여야 합니다');
    }

    const mode = this.registry.get(input.gameMode);
    const questions = await this.pool.pickRandom(
      {
        topic: input.topic,
        week: input.week,
        gameMode: input.gameMode,
        difficulty: input.difficulty,
      },
      input.rounds,
    );

    if (questions.length === 0) {
      throw new BadRequestException(
        `해당 조건의 활성 문제가 없습니다 (topic=${input.topic}, week=${input.week}, mode=${input.gameMode})`,
      );
    }

    const timeLimit = DEFAULT_TIME_LIMIT_BY_DIFFICULTY[input.difficulty];

    const rounds = questions.map((question) =>
      mode.generateRound(question, {
        topic: input.topic,
        week: input.week,
        difficulty: input.difficulty,
        timeLimit,
      }),
    );

    for (const round of rounds) {
      this.activeRounds.set(round.id, round);
    }

    return rounds;
  }

  submitAnswer(answer: PlayerAnswer) {
    const round = this.activeRounds.get(answer.roundId);
    if (!round) {
      throw new BadRequestException(`Round ${answer.roundId} not found or expired`);
    }
    const mode = this.registry.get(round.question.gameMode);
    const result = mode.evaluateAnswer(round, answer);
    this.activeRounds.delete(answer.roundId);
    return result;
  }
}
