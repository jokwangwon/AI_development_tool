import type { Topic } from '@oracle-game/shared';

/**
 * 1주차 sql-basics 학습 범위 (키워드 화이트리스트)
 *
 * SDD §4.2 + 헌법 §3: 이 화이트리스트에 없는 Oracle 식별자가 문제에
 * 등장하면 ScopeValidator가 폐기한다 (계산적 검증).
 *
 * 검증 정규식: `\b[A-Z][A-Z_0-9]{1,}\b` (대문자 시작, 2글자 이상)
 *
 * 따라서 여기에는 **2글자 이상의 대문자 토큰**만 등록한다. 한국어 텍스트나
 * 소문자, 단일 대문자(A, I 등)는 검증 대상이 아니므로 등록 불필요.
 */

export interface WeeklyScopeSeed {
  week: number;
  topic: Topic;
  keywords: string[];
  sourceUrl: string | null;
}

const KEYWORDS_WEEK1_SQL_BASICS: string[] = [
  // --- DML 기본 ---
  'SELECT',
  'FROM',
  'WHERE',
  'AS',
  'DISTINCT',

  // --- 정렬 ---
  'ORDER',
  'BY',
  'ASC',
  'DESC',

  // --- 그룹 / 집계 ---
  'GROUP',
  'HAVING',
  'COUNT',
  'SUM',
  'AVG',
  'MAX',
  'MIN',

  // --- 비교 / 논리 / NULL ---
  'AND',
  'OR',
  'NOT',
  'IS',
  'IN',
  'BETWEEN',
  'LIKE',
  'NULL',

  // --- 집합 연산 ---
  'UNION',
  'ALL',
  'MINUS',
  'INTERSECT',

  // --- Oracle 특수 ---
  'DUAL',

  // --- 예시 테이블 ---
  'EMP',
  'EMPLOYEES',
  'DEPT',
  'DEPARTMENTS',

  // --- 예시 컬럼 (Oracle 전통 EMP/DEPT 스키마) ---
  'ENAME',
  'EMPNO',
  'JOB',
  'MGR',
  'HIREDATE',
  'SAL',
  'COMM',
  'DEPTNO',
  'DNAME',
  'LOC',
];

export const WEEK1_SQL_BASICS_SCOPE: WeeklyScopeSeed = {
  week: 1,
  topic: 'sql-basics',
  keywords: KEYWORDS_WEEK1_SQL_BASICS,
  sourceUrl: null,
};
