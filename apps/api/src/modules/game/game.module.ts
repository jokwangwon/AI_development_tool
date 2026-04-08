import { Module } from '@nestjs/common';

import { ContentModule } from '../content/content.module';
import { GameController } from './game.controller';
import { GameSessionService } from './services/game-session.service';
import { GameModeRegistry } from './modes/game-mode.registry';
import { BlankTypingMode } from './modes/blank-typing.mode';
import { TermMatchMode } from './modes/term-match.mode';

@Module({
  imports: [ContentModule],
  providers: [
    GameSessionService,
    GameModeRegistry,
    BlankTypingMode,
    TermMatchMode,
  ],
  controllers: [GameController],
})
export class GameModule {}
