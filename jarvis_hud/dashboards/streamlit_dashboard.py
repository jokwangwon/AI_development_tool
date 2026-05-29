import streamlit as st
import json
import os
import urllib.request
import urllib.error
import pandas as pd
import datetime
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.jarvis import paths  # §10-2 영속 위치 일원화 (JARVIS_DATA_DIR > XDG)

st.set_page_config(page_title="Jarvis 자비스 상태", layout="wide")
st.title("자비스 상태 dashboard")
st.caption(f"현재 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

st.markdown('<meta http-equiv="refresh" content="10">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("[1] Ollama 사장")
    try:
        with urllib.request.urlopen("http://localhost:11434/api/tags", timeout=3) as response:
            data = json.loads(response.read().decode())
            model_count = len(data.get("models", []))
            st.metric("daemon", "UP")
            st.metric("모델 수", model_count)
            st.write("모델 목록:")
            for model in data["models"]:
                st.write(f"- {model['name']}")
    except Exception as e:
        st.metric("daemon", "DOWN", delta="-1", delta_color="inverse")

    st.subheader("[2] Layer 0 관찰")
    try:
        file_path = str(paths.layer0_memory_path())
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                lines = f.readlines()
            entry_count = len(lines)
            st.metric("entries", entry_count)
            if lines:
                last_entries = [json.loads(line.strip()) for line in lines[-3:]]
                df = pd.DataFrame(last_entries)
                st.dataframe(df)
        else:
            st.info("자료 없음")
    except Exception as e:
        st.info("자료 없음")

with col2:
    st.subheader("[3] Layer 1 axis 자료")
    try:
        file_path = str(paths.layer1_report_path())
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
            advice_axis_stats = data.get("advice_axis_stats", {})
            if advice_axis_stats:
                df = pd.DataFrame(advice_axis_stats).T
                st.dataframe(df)
            else:
                st.info("자료 없음")
        else:
            st.info("자료 없음")
    except Exception as e:
        st.info("자료 없음")

    st.subheader("[4] 최신 모델 측정")
    try:
        file_path = str(paths.multi_model_measurement_path())
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
            models = data.get("models", [])
            if models:
                model_stats = []
                for model in models:
                    if model.get("skipped"):
                        continue
                    model_name = model["model"]
                    decode_tok_per_s = model.get("stats", {}).get("decode_tok_per_s", {})
                    mean_decode = decode_tok_per_s.get("mean", 0.0)
                    model_stats.append({"model": model_name, "decode_tok_per_s_mean": mean_decode})
                df = pd.DataFrame(model_stats).sort_values(by="decode_tok_per_s_mean", ascending=False)
                st.bar_chart(df.set_index('model'))
            else:
                st.info("자료 없음")
        else:
            st.info("자료 없음")
    except Exception as e:
        st.info("자료 없음")