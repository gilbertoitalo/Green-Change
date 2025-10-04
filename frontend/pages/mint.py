import os, requests, streamlit as st

st.set_page_config(page_title="Mint", layout="wide")
BASE = st.secrets.get("BACKEND_BASE_URL", os.getenv("BACKEND_BASE_URL", "http://127.0.0.1:8000"))

st.title("🪙 Mint de Crédito (mock)")
st.caption("Este ambiente está em modo mock. Quando virar on-chain, aparecerá o link do Etherscan.")

with st.form("mint_form"):
    to_address = st.text_input("Carteira (0x...)", placeholder="0xabc...")
    km = st.number_input("Distância (km)", min_value=0.0, step=1.0, value=50.0, format="%.2f")
    submitted = st.form_submit_button("Mint")

if submitted:
    try:
        r = requests.post(f"{BASE}/credits/mint", json={"to_address": to_address, "distance_km": km}, timeout=20)
        if r.status_code == 422:
            st.error("Endereço Ethereum inválido (422).")
        r.raise_for_status()
        data = r.json()
        st.success("Mint solicitado!")
        st.json(data)
        if data.get("explorer"):
            st.link_button("Ver no Etherscan", data["explorer"])
    except Exception as e:
        st.error(f"Erro ao consultar API: {e}")
