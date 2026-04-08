'use client';

import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import {
  CURRICULUM_TOPICS,
  GAME_MODE_LABELS,
  TOPIC_LABELS,
  type Difficulty,
  type EvaluationResult,
  type GameModeId,
  type Round,
  type Topic,
} from '@oracle-game/shared';
import { apiClient } from '@/lib/api-client';

type Phase = 'config' | 'playing' | 'finished';

export default function SoloPlayPage() {
  const [phase, setPhase] = useState<Phase>('config');
  const [topic, setTopic] = useState<Topic>('sql-basics');
  const [week, setWeek] = useState(1);
  const [gameMode, setGameMode] = useState<GameModeId>('blank-typing');
  const [difficulty, setDifficulty] = useState<Difficulty>('EASY');
  const [rounds, setRounds] = useState<Round[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [results, setResults] = useState<EvaluationResult[]>([]);
  const [error, setError] = useState<string | null>(null);

  // 데모 단계: 토큰은 임시 localStorage 기반
  const token = useMemo(
    () => (typeof window !== 'undefined' ? localStorage.getItem('token') ?? '' : ''),
    [],
  );

  const startGame = useCallback(async () => {
    setError(null);
    try {
      const data = await apiClient.solo.start(token, {
        topic,
        week,
        gameMode,
        difficulty,
        rounds: 10,
      });
      setRounds(data);
      setResults([]);
      setCurrentIndex(0);
      setPhase('playing');
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Unknown error');
    }
  }, [token, topic, week, gameMode, difficulty]);

  if (phase === 'config') {
    return (
      <Container>
        <h1 style={{ fontSize: '1.75rem', marginBottom: '1.5rem' }}>솔로 플레이 설정</h1>

        <Field label="주제">
          <select value={topic} onChange={(e) => setTopic(e.target.value as Topic)}>
            {CURRICULUM_TOPICS.map((t) => (
              <option key={t} value={t}>
                {TOPIC_LABELS[t]}
              </option>
            ))}
          </select>
        </Field>

        <Field label="주차">
          <input
            type="number"
            min={1}
            value={week}
            onChange={(e) => setWeek(Number.parseInt(e.target.value, 10))}
          />
        </Field>

        <Field label="게임 모드">
          <select
            value={gameMode}
            onChange={(e) => setGameMode(e.target.value as GameModeId)}
          >
            <option value="blank-typing">{GAME_MODE_LABELS['blank-typing']}</option>
            <option value="term-match">{GAME_MODE_LABELS['term-match']}</option>
          </select>
        </Field>

        <Field label="난이도">
          <select
            value={difficulty}
            onChange={(e) => setDifficulty(e.target.value as Difficulty)}
          >
            <option value="EASY">EASY</option>
            <option value="MEDIUM">MEDIUM</option>
            <option value="HARD">HARD</option>
          </select>
        </Field>

        <button
          type="button"
          onClick={startGame}
          style={{
            marginTop: '1.5rem',
            padding: '0.75rem 1.5rem',
            background: 'var(--accent)',
            border: 'none',
            borderRadius: 8,
            color: '#0f172a',
            fontWeight: 700,
          }}
        >
          시작하기
        </button>
        {error && <p style={{ color: 'var(--error)', marginTop: '1rem' }}>{error}</p>}
      </Container>
    );
  }

  if (phase === 'playing') {
    const current = rounds[currentIndex];
    if (!current) {
      return (
        <Container>
          <p>라운드를 불러오는 중...</p>
        </Container>
      );
    }
    return (
      <RoundPlayer
        round={current}
        token={token}
        roundNumber={currentIndex + 1}
        totalRounds={rounds.length}
        onComplete={(result) => {
          setResults((prev) => [...prev, result]);
          if (currentIndex + 1 >= rounds.length) {
            setPhase('finished');
          } else {
            setCurrentIndex(currentIndex + 1);
          }
        }}
      />
    );
  }

  // finished
  const totalScore = results.reduce((sum, r) => sum + r.score, 0);
  const correctCount = results.filter((r) => r.isCorrect).length;
  return (
    <Container>
      <h1 style={{ fontSize: '1.75rem', marginBottom: '1rem' }}>게임 종료</h1>
      <p style={{ marginBottom: '0.5rem' }}>
        정답률: {correctCount} / {results.length} (
        {Math.round((correctCount / Math.max(1, results.length)) * 100)}%)
      </p>
      <p style={{ marginBottom: '1.5rem' }}>총 점수: {totalScore}</p>
      <button
        type="button"
        onClick={() => setPhase('config')}
        style={{
          padding: '0.75rem 1.5rem',
          background: 'var(--accent)',
          border: 'none',
          borderRadius: 8,
          color: '#0f172a',
          fontWeight: 700,
        }}
      >
        다시 플레이
      </button>
    </Container>
  );
}

function RoundPlayer({
  round,
  token,
  roundNumber,
  totalRounds,
  onComplete,
}: {
  round: Round;
  token: string;
  roundNumber: number;
  totalRounds: number;
  onComplete: (result: EvaluationResult) => void;
}) {
  const [answer, setAnswer] = useState('');
  const [hintsUsed, setHintsUsed] = useState(0);
  const [error, setError] = useState<string | null>(null);
  const startedAt = useRef(Date.now());

  useEffect(() => {
    setAnswer('');
    setHintsUsed(0);
    startedAt.current = Date.now();
  }, [round.id]);

  const submit = async () => {
    setError(null);
    try {
      const result = await apiClient.solo.answer(token, {
        roundId: round.id,
        answer,
        submittedAt: Date.now() - startedAt.current,
        hintsUsed,
      });
      onComplete(result);
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Unknown error');
    }
  };

  const content = round.question.content;

  return (
    <Container>
      <p style={{ color: 'var(--fg-muted)', marginBottom: '0.5rem' }}>
        라운드 {roundNumber} / {totalRounds}
      </p>

      {content.type === 'blank-typing' && (
        <pre
          style={{
            background: 'var(--bg-elevated)',
            padding: '1.25rem',
            borderRadius: 8,
            marginBottom: '1.5rem',
            fontSize: '1rem',
            whiteSpace: 'pre-wrap',
          }}
        >
          {content.sql}
        </pre>
      )}

      {content.type === 'term-match' && (
        <p
          style={{
            background: 'var(--bg-elevated)',
            padding: '1.25rem',
            borderRadius: 8,
            marginBottom: '1.5rem',
            fontSize: '1.1rem',
          }}
        >
          {content.description}
        </p>
      )}

      <input
        type="text"
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === 'Enter') submit();
        }}
        placeholder="정답을 입력하세요"
        style={{
          width: '100%',
          padding: '0.75rem 1rem',
          background: 'var(--bg-elevated)',
          border: '1px solid var(--border)',
          borderRadius: 8,
          color: 'var(--fg)',
        }}
        autoFocus
      />

      <div style={{ marginTop: '1rem', display: 'flex', gap: '0.5rem' }}>
        <button
          type="button"
          onClick={submit}
          style={{
            padding: '0.6rem 1.25rem',
            background: 'var(--accent)',
            border: 'none',
            borderRadius: 8,
            color: '#0f172a',
            fontWeight: 700,
          }}
        >
          제출
        </button>
        {hintsUsed < round.hints.length && (
          <button
            type="button"
            onClick={() => setHintsUsed(hintsUsed + 1)}
            style={{
              padding: '0.6rem 1.25rem',
              background: 'var(--bg-elevated)',
              border: '1px solid var(--border)',
              borderRadius: 8,
              color: 'var(--fg)',
            }}
          >
            힌트 보기 ({hintsUsed + 1}/{round.hints.length})
          </button>
        )}
      </div>

      {hintsUsed > 0 && (
        <ul
          style={{
            marginTop: '1rem',
            padding: '0.75rem 1rem',
            background: 'var(--bg-elevated)',
            borderRadius: 8,
            listStyle: 'disc inside',
            color: 'var(--fg-muted)',
          }}
        >
          {round.hints.slice(0, hintsUsed).map((h, i) => (
            <li key={i}>{h}</li>
          ))}
        </ul>
      )}

      {error && <p style={{ color: 'var(--error)', marginTop: '1rem' }}>{error}</p>}
    </Container>
  );
}

function Container({ children }: { children: React.ReactNode }) {
  return (
    <main
      style={{
        maxWidth: 720,
        margin: '0 auto',
        padding: '3rem 1.5rem',
      }}
    >
      {children}
    </main>
  );
}

function Field({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <label
      style={{
        display: 'block',
        marginBottom: '1rem',
      }}
    >
      <span style={{ display: 'block', color: 'var(--fg-muted)', marginBottom: '0.25rem' }}>
        {label}
      </span>
      {children}
    </label>
  );
}
