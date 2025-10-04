import os, requests, streamlit as st

st.set_page_config(page_title="Simulador", layout="wide")
BASE = st.secrets.get("BACKEND_BASE_URL", os.getenv("BACKEND_BASE_URL", "http://127.0.0.1:8000"))

st.title("Calcule sua pegada de carbono")
st.write("Preencha os dados abaixo para simular seu impacto ambiental:")

with st.form("simulador_form"):
    km = st.number_input("Quilômetros (km)", min_value=0.0, step=1.0, value=100.0, format="%.2f")
    submitted = st.form_submit_button("Calcular")

if submitted:
    try:
        r = requests.post(f"{BASE}/credits/simulate", json={"distance_km": km}, timeout=10)
        r.raise_for_status()
        data = r.json()
        st.success("Cálculo realizado!")
        st.metric("CO₂ evitado (kg)", f"{data['co2_credits_kg']:.2f}")
        st.metric("Distância (km)", f"{data['distance_km']:.2f}")
    except Exception as e:
        st.error(f"Erro ao consultar API: {e}")


