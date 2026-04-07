// ============================================
// C# 기초 Lesson 1: Python/JS 개발자를 위한 속성 가이드
// ============================================

using System;
using System.Collections.Generic;

// ─── 1. 변수 선언 ───────────────────────────
// Python: name = "마을이"        (타입 없음)
// JS:     let name = "마을이";   (let/const)
// C#:     string name = "마을이"; (타입 명시 필수!)

// ─── 2. 기본 타입 ───────────────────────────
// Python/JS에는 없는 개념: C#은 "정적 타입" 언어
// 한번 타입을 정하면 바꿀 수 없음

class Lesson1_Variables
{
    public static void Run()
    {
        Console.WriteLine("=== Lesson 1: 변수와 타입 ===\n");

        // 기본 타입들
        string npcName = "마을이";      // 문자열 (Python: str, JS: string)
        int population = 5;             // 정수 (Python: int, JS: number)
        float happiness = 75.5f;        // 소수점 (f 붙여야 함! Unity에서 주로 사용)
        bool isRaining = false;         // 참/거짓 (Python: True/False)

        Console.WriteLine($"NPC 이름: {npcName}");         // f-string과 동일! $ 사용
        Console.WriteLine($"인구: {population}명");
        Console.WriteLine($"행복도: {happiness}%");
        Console.WriteLine($"비 오는 중: {isRaining}");

        // var = 타입 추론 (Python/JS의 let과 비슷)
        var villageLevel = 1;  // 컴파일러가 int로 추론
        Console.WriteLine($"마을 레벨: {villageLevel}");

        Console.WriteLine();
    }
}

// ─── 3. 조건문 ───────────────────────────────
// Python: if / elif / else (들여쓰기)
// JS:     if / else if / else { }
// C#:     if / else if / else { }  ← JS와 거의 동일!

class Lesson2_Conditions
{
    public static void Run()
    {
        Console.WriteLine("=== Lesson 2: 조건문 ===\n");

        float happiness = 75.5f;

        if (happiness >= 80)
        {
            Console.WriteLine("주민들이 매우 행복합니다!");
        }
        else if (happiness >= 50)
        {
            Console.WriteLine("주민들이 보통 상태입니다.");
        }
        else
        {
            Console.WriteLine("주민들이 불행합니다...");
        }

        // switch문 — Unity FSM에서 핵심적으로 사용!
        string weather = "Rain";

        switch (weather)
        {
            case "Rain":
                Console.WriteLine("비가 옵니다 -> 주민들이 밭에 물을 줍니다");
                break;
            case "Sun":
                Console.WriteLine("햇빛이 강합니다 -> 주민들이 빨래를 널습니다");
                break;
            case "Wind":
                Console.WriteLine("바람이 붑니다 -> 풍차가 돌아갑니다");
                break;
            default:
                Console.WriteLine("맑은 날씨 -> 평화로운 하루");
                break;
        }

        Console.WriteLine();
    }
}

// ─── 4. 반복문 ───────────────────────────────

class Lesson3_Loops
{
    public static void Run()
    {
        Console.WriteLine("=== Lesson 3: 반복문 ===\n");

        // for문 — JS와 동일
        Console.WriteLine("NPC 생성 중...");
        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine($"  NPC #{i + 1} 생성 완료");
        }

        // foreach — Python의 for item in list 와 동일
        string[] jobs = { "농부", "건축가", "탐험가", "요리사" };

        Console.WriteLine("\n직업 목록:");
        foreach (string job in jobs)
        {
            Console.WriteLine($"  - {job}");
        }

        // List<T> — Python의 list와 동일, 하지만 타입을 지정해야 함
        List<string> npcNames = new List<string> { "마을이", "들판이", "언덕이" };
        npcNames.Add("강가이");  // Python: append()

        Console.WriteLine($"\n전체 NPC 수: {npcNames.Count}");  // Python: len()

        Console.WriteLine();
    }
}

// ─── 5. 함수 (메서드) ─────────────────────────

class Lesson4_Methods
{
    // Python: def greet(name):
    // JS:     function greet(name) { }
    // C#:     반환타입 메서드이름(타입 매개변수)

    static string GetGreeting(string npcName, string job)
    {
        return $"안녕! 나는 {npcName}, 직업은 {job}야!";
    }

    // void = 반환값 없음 (Python: return 없는 함수)
    static void PrintWeatherEffect(string weather)
    {
        Console.WriteLine($"[날씨 효과] {weather} 적용 중...");
    }

    // 기본값 매개변수 — Python과 동일!
    static float CalculateHappiness(float baseHappiness, float weatherBonus = 0f)
    {
        return Math.Clamp(baseHappiness + weatherBonus, 0f, 100f);
    }

    public static void Run()
    {
        Console.WriteLine("=== Lesson 4: 함수(메서드) ===\n");

        string greeting = GetGreeting("마을이", "농부");
        Console.WriteLine(greeting);

        PrintWeatherEffect("비");

        float happy = CalculateHappiness(70f, 15f);
        Console.WriteLine($"행복도: {happy}");

        float defaultHappy = CalculateHappiness(50f);  // 기본값 사용
        Console.WriteLine($"기본 행복도: {defaultHappy}");

        Console.WriteLine();
    }
}

// ─── 6. 클래스 — Unity의 핵심! ─────────────────

// Python:
//   class NPC:
//       def __init__(self, name, job):
//           self.name = name
//           self.job = job
//
// C#: 훨씬 명시적이지만 구조는 같다

class NPC
{
    // 필드 (Python의 self.xxx)
    public string Name;
    public string Job;
    public float Happiness;
    public float Energy;

    // 생성자 (Python의 __init__)
    public NPC(string name, string job)
    {
        Name = name;
        Job = job;
        Happiness = 50f;
        Energy = 100f;
    }

    // 메서드
    public void Work()
    {
        Energy -= 10f;
        Console.WriteLine($"  {Name}({Job})이 일합니다. 에너지: {Energy}");
    }

    public void Rest()
    {
        Energy += 20f;
        if (Energy > 100f) Energy = 100f;
        Console.WriteLine($"  {Name}이 휴식합니다. 에너지: {Energy}");
    }

    public void ReactToWeather(string weather)
    {
        switch (weather)
        {
            case "Rain":
                if (Job == "농부")
                {
                    Happiness += 10f;
                    Console.WriteLine($"  {Name}: \"비다! 밭에 물주자!\" (행복도 +10)");
                }
                else
                {
                    Happiness -= 5f;
                    Console.WriteLine($"  {Name}: \"비가 오네... 실내로 들어가자\" (행복도 -5)");
                }
                break;
            case "Sun":
                Happiness += 5f;
                Console.WriteLine($"  {Name}: \"날이 좋다!\" (행복도 +5)");
                break;
        }
    }

    // ToString — Python의 __str__
    public override string ToString()
    {
        return $"[{Name}] 직업:{Job} 행복:{Happiness} 에너지:{Energy}";
    }
}

class Lesson5_Classes
{
    public static void Run()
    {
        Console.WriteLine("=== Lesson 5: 클래스 (Unity의 핵심) ===\n");

        NPC farmer = new NPC("마을이", "농부");
        NPC builder = new NPC("들판이", "건축가");
        NPC explorer = new NPC("언덕이", "탐험가");

        Console.WriteLine("--- NPC 초기 상태 ---");
        Console.WriteLine(farmer);
        Console.WriteLine(builder);
        Console.WriteLine(explorer);

        Console.WriteLine("\n--- 비가 내립니다 ---");
        farmer.ReactToWeather("Rain");
        builder.ReactToWeather("Rain");
        explorer.ReactToWeather("Rain");

        Console.WriteLine("\n--- NPC 활동 ---");
        farmer.Work();
        farmer.Work();
        farmer.Rest();

        Console.WriteLine("\n--- 최종 상태 ---");
        Console.WriteLine(farmer);
        Console.WriteLine(builder);
        Console.WriteLine(explorer);

        Console.WriteLine();
    }
}

// ─── 7. enum — Unity에서 상태 관리의 핵심 ──────

enum NPCState
{
    Sleeping,
    Idle,
    Working,
    Eating,
    Exploring,
    Resting
}

enum Weather
{
    Clear,
    Rain,
    Sun,
    Wind,
    Winter
}

class Lesson6_Enums
{
    public static void Run()
    {
        Console.WriteLine("=== Lesson 6: Enum (FSM의 기초) ===\n");

        NPCState currentState = NPCState.Sleeping;
        Weather currentWeather = Weather.Clear;

        Console.WriteLine($"NPC 상태: {currentState}");
        Console.WriteLine($"현재 날씨: {currentWeather}");

        // 상태 전환 시뮬레이션 (이것이 FSM의 본질!)
        Console.WriteLine("\n--- 시간이 흐릅니다... ---");

        currentState = NPCState.Idle;
        Console.WriteLine($"아침 -> 상태 변경: {currentState}");

        currentWeather = Weather.Rain;
        Console.WriteLine($"비 버튼 ON -> 날씨 변경: {currentWeather}");

        // 날씨에 따라 상태 결정 (이것이 우리 게임의 핵심 로직!)
        if (currentWeather == Weather.Rain)
        {
            currentState = NPCState.Working;
            Console.WriteLine($"비가 오니까 -> 상태 변경: {currentState} (밭에 물주기)");
        }

        Console.WriteLine();
    }
}

// ─── 메인 실행 ─────────────────────────────────

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("==========================================");
        Console.WriteLine("  미니어처 갓 핸드 - C# 기초 학습");
        Console.WriteLine("  Python/JS 개발자를 위한 속성 가이드");
        Console.WriteLine("==========================================\n");

        Lesson1_Variables.Run();
        Lesson2_Conditions.Run();
        Lesson3_Loops.Run();
        Lesson4_Methods.Run();
        Lesson5_Classes.Run();
        Lesson6_Enums.Run();

        Console.WriteLine("기초 문법 레슨 완료!\n");

        // Lesson 2: Unity 패턴 시뮬레이션
        GameSimulation.Run();
    }
}
