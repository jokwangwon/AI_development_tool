// ============================================
// C# Lesson 2: Unity 핵심 패턴 (서버에서 시뮬레이션)
// ============================================
// Unity 없이도 핵심 패턴을 이해할 수 있도록
// Unity API를 흉내내는 시뮬레이션 코드로 학습합니다.
// 이 코드의 구조가 그대로 Unity에서 사용됩니다.

using System;
using System.Collections.Generic;

// ═══════════════════════════════════════════════
// Part 1: Unity의 MonoBehaviour 시뮬레이션
// ═══════════════════════════════════════════════
//
// Unity에서 모든 게임 오브젝트에 붙는 스크립트는
// MonoBehaviour를 상속받습니다.
//
// Python으로 비유하면:
//   class MyScript(MonoBehaviour):  ← 상속
//       def start(self):            ← 게임 시작 시 1번
//       def update(self):           ← 매 프레임 호출
//
// JS로 비유하면:
//   class MyScript extends MonoBehaviour {
//       start() { }   // 초기화
//       update() { }  // 매 프레임 (requestAnimationFrame과 유사)
//   }

// Unity의 MonoBehaviour를 흉내내는 기반 클래스
abstract class SimulatedMonoBehaviour
{
    public string gameObjectName = "GameObject";
    public bool enabled = true;

    // Unity 라이프사이클 메서드들
    public virtual void Awake() { }     // 오브젝트 생성 시 (가장 먼저)
    public virtual void Start() { }     // 첫 프레임 직전 (Awake 다음)
    public virtual void Update() { }    // 매 프레임 호출 (핵심!)
}

// ═══════════════════════════════════════════════
// Part 2: 우리 게임의 TimeManager
// ═══════════════════════════════════════════════
// 게임 내 시간을 관리하는 싱글톤 매니저
// Unity에서는 이것이 하나의 GameObject에 붙는 컴포넌트

class TimeManager : SimulatedMonoBehaviour
{
    // 싱글톤 패턴 — 게임 전체에서 하나만 존재
    // Python: 클래스 변수로 구현
    // JS: static 또는 모듈 패턴
    public static TimeManager Instance { get; private set; }

    // [SerializeField] — Unity 에디터에서 값을 조절할 수 있게 해주는 속성
    // Python에는 없는 개념. Unity의 Inspector 창에서 드래그로 값 변경 가능
    /* [SerializeField] */ private float minutesPerRealSecond = 120f;

    // 게임 내 시간
    public int Hour { get; private set; }
    public int Minute { get; private set; }
    public int Day { get; private set; }

    // 시간대 (enum 활용!)
    public TimeOfDay CurrentTimeOfDay
    {
        get
        {
            if (Hour >= 5 && Hour < 7) return TimeOfDay.Dawn;
            if (Hour >= 7 && Hour < 12) return TimeOfDay.Morning;
            if (Hour >= 12 && Hour < 17) return TimeOfDay.Afternoon;
            if (Hour >= 17 && Hour < 20) return TimeOfDay.Evening;
            return TimeOfDay.Night;
        }
    }

    // 이벤트 — 시간이 변할 때 다른 시스템에 알림
    // Python의 callback list, JS의 EventEmitter와 유사
    public event Action<int> OnHourChanged;
    public event Action<TimeOfDay> OnTimeOfDayChanged;

    private float accumulatedTime = 0f;
    private TimeOfDay lastTimeOfDay;

    public override void Awake()
    {
        Instance = this;   // 싱글톤 등록
        Hour = 6;          // 새벽 6시 시작
        Minute = 0;
        Day = 1;
        lastTimeOfDay = CurrentTimeOfDay;
    }

    public override void Update()
    {
        // 실제 Unity에서는 Time.deltaTime 사용
        // 여기서는 시뮬레이션으로 1초씩 진행
        float deltaTime = 1f;

        accumulatedTime += deltaTime * minutesPerRealSecond;

        while (accumulatedTime >= 60f)
        {
            accumulatedTime -= 60f;
            Minute++;

            if (Minute >= 60)
            {
                Minute = 0;
                Hour++;
                OnHourChanged?.Invoke(Hour);  // 이벤트 발생!

                if (Hour >= 24)
                {
                    Hour = 0;
                    Day++;
                }
            }
        }

        // 시간대가 바뀌면 알림
        var currentTOD = CurrentTimeOfDay;
        if (currentTOD != lastTimeOfDay)
        {
            OnTimeOfDayChanged?.Invoke(currentTOD);
            lastTimeOfDay = currentTOD;
        }
    }

    public override string ToString()
    {
        return $"Day {Day}, {Hour:D2}:{Minute:D2} ({CurrentTimeOfDay})";
    }
}

enum TimeOfDay
{
    Dawn,       // 새벽 (5-7)
    Morning,    // 오전 (7-12)
    Afternoon,  // 오후 (12-17)
    Evening,    // 저녁 (17-20)
    Night       // 밤 (20-5)
}

// ═══════════════════════════════════════════════
// Part 3: WeatherManager — 우리 게임의 핵심!
// ═══════════════════════════════════════════════
// 플레이어가 토글하는 환경 버튼을 관리

enum WeatherType
{
    Clear,    // 맑음 (기본)
    Rain,     // 비
    Sun,      // 강한 햇빛
    Wind,     // 바람
    Winter    // 겨울/눈
}

class WeatherManager : SimulatedMonoBehaviour
{
    public static WeatherManager Instance { get; private set; }

    public WeatherType CurrentWeather { get; private set; } = WeatherType.Clear;

    // 이벤트 — 날씨 변경 시 NPC들에게 알림
    public event Action<WeatherType> OnWeatherChanged;

    public override void Awake()
    {
        Instance = this;
    }

    // 플레이어가 버튼을 누르면 호출되는 메서드
    public void ToggleWeather(WeatherType weather)
    {
        if (CurrentWeather == weather)
        {
            // 같은 버튼 다시 누르면 OFF → 맑음으로
            CurrentWeather = WeatherType.Clear;
        }
        else
        {
            // 다른 버튼 누르면 해당 날씨로 변경
            CurrentWeather = weather;
        }

        Console.WriteLine($"  [날씨 변경] → {CurrentWeather}");
        OnWeatherChanged?.Invoke(CurrentWeather);  // 모든 구독자에게 알림!
    }
}

// ═══════════════════════════════════════════════
// Part 4: NPCController — FSM 실전 구현
// ═══════════════════════════════════════════════
// 이것이 실제 Unity에서 NPC에 붙는 스크립트의 구조

enum NPCStateType
{
    Sleeping,
    Idle,
    Working,
    Eating,
    Exploring,
    Resting
}

// NPC 성격 — 행동에 영향
enum Personality
{
    Diligent,    // 부지런 — 일찍 시작, 오래 일함
    Relaxed,     // 느긋 — 늦게 시작, 자주 쉼
    Curious      // 호기심 — 탐험 자주
}

class NPCController : SimulatedMonoBehaviour
{
    // NPC 기본 정보
    public string NpcName;
    public string Job;
    public Personality PersonalityType;

    // 상태
    public NPCStateType CurrentState { get; private set; }
    public float Energy = 100f;
    public float Happiness = 50f;
    public float Hunger = 0f;

    // 랜덤화 — Agent B가 "처음부터 넣어라"고 했던 것!
    private Random rng = new Random();
    private int scheduleOffset;  // 스케줄 ±편차 (분)

    public NPCController(string name, string job, Personality personality)
    {
        NpcName = name;
        Job = job;
        PersonalityType = personality;
        gameObjectName = name;

        // 성격에 따른 스케줄 편차
        scheduleOffset = personality switch
        {
            Personality.Diligent => rng.Next(-15, 0),    // 부지런 → 일찍
            Personality.Relaxed => rng.Next(0, 30),      // 느긋 → 늦게
            Personality.Curious => rng.Next(-5, 15),     // 호기심 → 약간 랜덤
            _ => 0
        };
    }

    public override void Start()
    {
        CurrentState = NPCStateType.Sleeping;

        // 날씨 변화를 구독 (옵저버 패턴)
        // Python: event_bus.subscribe("weather_changed", self.on_weather)
        // JS: weatherManager.addEventListener("change", this.onWeather)
        WeatherManager.Instance.OnWeatherChanged += OnWeatherChanged;

        // 시간 변화를 구독
        TimeManager.Instance.OnHourChanged += OnHourChanged;
    }

    // ─── FSM 핵심: 매 프레임 상태 평가 ───
    public override void Update()
    {
        // 상태별 에너지/배고픔 변화
        switch (CurrentState)
        {
            case NPCStateType.Working:
                Energy -= 0.5f;
                Hunger += 0.3f;
                break;
            case NPCStateType.Exploring:
                Energy -= 0.3f;
                Hunger += 0.2f;
                break;
            case NPCStateType.Resting:
                Energy += 1f;
                break;
            case NPCStateType.Sleeping:
                Energy += 2f;
                break;
            case NPCStateType.Eating:
                Hunger -= 2f;
                break;
        }

        // 값 제한 (Clamp)
        Energy = Math.Clamp(Energy, 0f, 100f);
        Hunger = Math.Clamp(Hunger, 0f, 100f);

        // 긴급 상태 전환 (배고픔/피로가 극심하면 강제 전환)
        if (Hunger >= 80f && CurrentState != NPCStateType.Eating)
        {
            TransitionTo(NPCStateType.Eating, "배가 너무 고프다!");
        }
        else if (Energy <= 10f && CurrentState != NPCStateType.Resting
                                && CurrentState != NPCStateType.Sleeping)
        {
            TransitionTo(NPCStateType.Resting, "너무 피곤하다...");
        }
    }

    // ─── 시간에 따른 상태 전환 ───
    private void OnHourChanged(int hour)
    {
        // 스케줄 편차 적용 (성격에 따라 다름)
        int adjustedHour = hour;

        switch (adjustedHour)
        {
            case 6:
            case 7:
                if (CurrentState == NPCStateType.Sleeping)
                {
                    TransitionTo(NPCStateType.Idle, "일어났다! 기지개~");
                }
                break;
            case 8:
            case 9:
                if (CurrentState == NPCStateType.Idle)
                {
                    var workState = PersonalityType == Personality.Curious
                        ? NPCStateType.Exploring
                        : NPCStateType.Working;
                    TransitionTo(workState, $"{Job} 시작!");
                }
                break;
            case 12:
                TransitionTo(NPCStateType.Eating, "점심 시간!");
                break;
            case 13:
                TransitionTo(NPCStateType.Working, "오후 작업 시작");
                break;
            case 18:
                TransitionTo(NPCStateType.Resting, "하루 일과 끝. 쉬자");
                break;
            case 21:
                TransitionTo(NPCStateType.Sleeping, "잘 시간이다...");
                break;
        }
    }

    // ─── 날씨에 따른 행동 변화 ───
    private void OnWeatherChanged(WeatherType weather)
    {
        // 잠자는 중이면 반응 안 함
        if (CurrentState == NPCStateType.Sleeping) return;

        switch (weather)
        {
            case WeatherType.Rain:
                if (Job == "농부")
                {
                    Happiness += 10f;
                    Console.WriteLine($"    {NpcName}: \"비다! 밭에 물주러 가자!\"");
                    TransitionTo(NPCStateType.Working, "비 맞으며 농사");
                }
                else
                {
                    Happiness -= 5f;
                    Console.WriteLine($"    {NpcName}: \"비가 오네... 안으로 들어가자\"");
                    TransitionTo(NPCStateType.Resting, "실내 대피");
                }
                break;

            case WeatherType.Sun:
                Happiness += 5f;
                Console.WriteLine($"    {NpcName}: \"날이 좋다!\"");
                if (Job == "건축가")
                    TransitionTo(NPCStateType.Working, "건설하기 좋은 날!");
                break;

            case WeatherType.Wind:
                Console.WriteLine($"    {NpcName}: \"바람이 분다~\"");
                if (Job == "탐험가")
                {
                    Happiness += 8f;
                    TransitionTo(NPCStateType.Exploring, "바람 따라 탐험!");
                }
                break;

            case WeatherType.Winter:
                Happiness -= 3f;
                Console.WriteLine($"    {NpcName}: \"춥다... 모닥불 근처로\"");
                TransitionTo(NPCStateType.Resting, "모닥불 근처에서 웅크림");
                break;

            case WeatherType.Clear:
                Console.WriteLine($"    {NpcName}: \"날씨가 개었네\"");
                break;
        }

        Happiness = Math.Clamp(Happiness, 0f, 100f);
    }

    // ─── 상태 전환 함수 ───
    private void TransitionTo(NPCStateType newState, string reason)
    {
        if (CurrentState == newState) return;

        var oldState = CurrentState;
        CurrentState = newState;
        Console.WriteLine($"    [{NpcName}] {oldState} → {newState} ({reason})");
    }

    public override string ToString()
    {
        return $"[{NpcName}] 직업:{Job}({PersonalityType}) " +
               $"상태:{CurrentState} 에너지:{Energy:F0} " +
               $"배고픔:{Hunger:F0} 행복:{Happiness:F0}";
    }
}

// ═══════════════════════════════════════════════
// Part 5: 게임 시뮬레이션 실행
// ═══════════════════════════════════════════════
// Unity의 게임 루프를 터미널에서 시뮬레이션

class GameSimulation
{
    public static void Run()
    {
        Console.WriteLine("==========================================");
        Console.WriteLine("  미니어처 갓 핸드 - 게임 시뮬레이션");
        Console.WriteLine("  Unity 패턴을 터미널에서 체험하기");
        Console.WriteLine("==========================================\n");

        // ─── 1. 매니저 초기화 (Unity: 씬에 빈 GameObject 배치) ───
        var timeManager = new TimeManager();
        var weatherManager = new WeatherManager();

        timeManager.Awake();
        weatherManager.Awake();

        // 시간대 변경 이벤트 구독
        timeManager.OnTimeOfDayChanged += (tod) =>
        {
            Console.WriteLine($"\n  ☀ 시간대 변경: {tod}");
        };

        // ─── 2. NPC 생성 (Unity: Prefab을 씬에 배치) ───
        var npcs = new List<NPCController>
        {
            new NPCController("마을이", "농부", Personality.Diligent),
            new NPCController("들판이", "건축가", Personality.Relaxed),
            new NPCController("언덕이", "탐험가", Personality.Curious),
            new NPCController("강가이", "요리사", Personality.Relaxed),
            new NPCController("바위돌", "농부", Personality.Diligent),
        };

        // Start 호출 (Unity: 첫 프레임)
        foreach (var npc in npcs) npc.Start();

        Console.WriteLine("--- NPC 5명 생성 완료 ---\n");

        // ─── 3. 게임 루프 시뮬레이션 ───
        // Unity에서는 이것이 자동으로 돌아감
        // 여기서는 24시간을 시뮬레이션

        Console.WriteLine("═══ 하루 시뮬레이션 시작 ═══\n");

        for (int tick = 0; tick < 200; tick++)
        {
            // Update 호출 (매 프레임)
            timeManager.Update();

            foreach (var npc in npcs)
            {
                npc.Update();
            }

            // 정시에만 시간 표시 (매분 출력하면 너무 많음)
            int prevHour = timeManager.Hour;
            // 시간 변경 감지는 이벤트로 처리됨

            // ─── 플레이어 조작 시뮬레이션 ───
            // 실제 게임에서는 버튼 클릭으로 동작

            // 오전 9시: 비 버튼 ON
            if (timeManager.Hour == 9 && weatherManager.CurrentWeather == WeatherType.Clear)
            {
                Console.WriteLine("\n  >> [플레이어] 비 버튼 ON");
                weatherManager.ToggleWeather(WeatherType.Rain);
            }

            // 오후 2시: 햇빛 ON
            if (timeManager.Hour == 14 && weatherManager.CurrentWeather == WeatherType.Rain)
            {
                Console.WriteLine("\n  >> [플레이어] 햇빛 버튼 ON");
                weatherManager.ToggleWeather(WeatherType.Sun);
            }

            // 저녁 6시: 겨울 ON
            if (timeManager.Hour == 18 && weatherManager.CurrentWeather != WeatherType.Winter)
            {
                Console.WriteLine("\n  >> [플레이어] 겨울 버튼 ON");
                weatherManager.ToggleWeather(WeatherType.Winter);
            }
        }

        // ─── 4. 하루 결산 ───
        Console.WriteLine("\n═══ 하루 결산 ═══\n");
        foreach (var npc in npcs)
        {
            Console.WriteLine(npc);
        }

        // ─── 핵심 학습 포인트 정리 ───
        Console.WriteLine("\n==========================================");
        Console.WriteLine("  핵심 학습 포인트");
        Console.WriteLine("==========================================");
        Console.WriteLine();
        Console.WriteLine("  1. MonoBehaviour 라이프사이클:");
        Console.WriteLine("     Awake() → Start() → Update() (매 프레임)");
        Console.WriteLine();
        Console.WriteLine("  2. 싱글톤 패턴:");
        Console.WriteLine("     TimeManager.Instance, WeatherManager.Instance");
        Console.WriteLine("     → 어디서든 접근 가능한 전역 매니저");
        Console.WriteLine();
        Console.WriteLine("  3. 이벤트/옵저버 패턴:");
        Console.WriteLine("     event Action<T> + OnWeatherChanged += handler");
        Console.WriteLine("     → 날씨 변하면 모든 NPC에게 자동 알림");
        Console.WriteLine();
        Console.WriteLine("  4. FSM (유한 상태 머신):");
        Console.WriteLine("     switch(CurrentState) + TransitionTo()");
        Console.WriteLine("     → 시간/날씨/상태에 따라 행동 전환");
        Console.WriteLine();
        Console.WriteLine("  5. [SerializeField]:");
        Console.WriteLine("     Unity 에디터에서 값 조절 가능하게 하는 속성");
        Console.WriteLine("     → 코드 수정 없이 밸런싱 가능!");
        Console.WriteLine();
    }
}
