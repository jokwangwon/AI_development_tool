import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime

def main():
    print("=== Jarvis 자비스 상태 ===")
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # Section [1] Ollama
    print("\n[1] Ollama:")
    try:
        with urllib.request.urlopen("http://localhost:11434/api/tags", timeout=3) as response:
            data = json.loads(response.read().decode())
            model_count = len(data.get("models", []))
            print(f"daemon: UP")
            print(f"모델 수: {model_count}")
    except Exception:
        print(f"daemon: DOWN")
        print(f"모델 수: 0")

    # Section [2] Layer 0
    print("\n[2] Layer 0:")
    layer0_path = "/tmp/jarvis-v00-layer0-memory.jsonl"
    try:
        if os.path.exists(layer0_path):
            with open(layer0_path, 'r') as f:
                lines = f.readlines()
                if lines:
                    last_line = json.loads(lines[-1])
                    if 'ts' in last_line:
                        print(f"최근 ts: {last_line['ts']}")
                    else:
                        print("최근 ts: 없음")
                else:
                    print("최근 ts: 없음")
        else:
            print("최근 ts: 없음")
    except Exception:
        print("최근 ts: 없음")

    # Section [3] Layer 1
    print("\n[3] Layer 1:")
    layer1_path = "/tmp/jarvis-v00-layer1-report.json"
    try:
        if os.path.exists(layer1_path):
            with open(layer1_path, 'r') as f:
                data = json.load(f)
                stats = data.get("advice_axis_stats", {})
                axes = ["의도 부합", "정확성", "위험 신호", "품질"]
                for axis in axes:
                    axis_stats = stats.get(axis, {})
                    ok = axis_stats.get("ok", 0)
                    warn = axis_stats.get("warn", 0)
                    fail = axis_stats.get("fail", 0)
                    none = axis_stats.get("none", 0)
                    unknown = axis_stats.get("unknown", 0)
                    print(f"  {axis}: ok={ok} warn={warn} fail={fail} none={none}")
        else:
            print("  (자료 없음)")
    except Exception:
        print("  (자료 없음)")

    # Section [4] 최신 측정
    print("\n[4] 최신 측정:")
    measurement_path = "/tmp/jarvis-v00-multi-model-measurement.json"
    try:
        if os.path.exists(measurement_path):
            with open(measurement_path, 'r') as f:
                data = json.load(f)
                models = data.get("models", [])
                # Sort by decode_tok_per_s.mean descending
                sorted_models = sorted(models, key=lambda x: x.get("stats", {}).get("decode_tok_per_s", {}).get("mean", 0), reverse=True)
                for i, model in enumerate(sorted_models):
                    mean_tok_per_s = model.get("stats", {}).get("decode_tok_per_s", {}).get("mean", 0)
                    model_name = model.get("model", "unknown")
                    print(f"  {i+1}위 {model_name}: {mean_tok_per_s:.2f} tok/s")
        else:
            print("  (자료 없음)")
    except Exception:
        print("  (자료 없음)")

if __name__ == "__main__":
    main()