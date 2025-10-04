import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Wallet - GreenCharge", layout="wide")

st.title("Sua Carteira de Créditos de Carbono")

# -------------------------
# Saldo e métricas principais
# -------------------------
st.markdown("### Resumo da Carteira")
saldo_total = 1250.00
creditos = 250
meta = 500
progresso = (creditos / meta) * 100

col1, col2, col3 = st.columns(3)
col1.metric("Saldo total", f"R$ {saldo_total:,.2f}")
col2.metric("Créditos de carbono", f"{creditos}")
col3.metric("CO₂ evitado", "1,2 ton")

st.markdown("---")

# -------------------------
# Gráfico de evolução (reduzido)
# -------------------------
st.markdown("### Evolução dos créditos")
df = pd.DataFrame({
    "Mes": ["Ago", "Set", "Out", "Nov", "Dez"],
    "Créditos acumulados": [120, 180, 250, 300, 400]
})

fig, ax = plt.subplots(figsize=(3.5, 2.0))  # gráfico bem pequeno
ax.plot(df["Mes"], df["Créditos acumulados"], marker="o", color="#2E86C1")
ax.set_xlabel("Mês", fontsize=8)
ax.set_ylabel("Créditos", fontsize=8)
ax.tick_params(axis="both", labelsize=8)
plt.tight_layout()
st.pyplot(fig)

st.markdown("---")

# -------------------------
# Progresso da meta mensal
# -------------------------
st.markdown("### Progresso da meta mensal")
st.write(f"Você já conquistou **{creditos}** de **{meta}** créditos")
st.progress(progresso / 100)

st.markdown("---")

# -------------------------
# Histórico de transações
# -------------------------
st.markdown("### Histórico de transações")
historico = pd.DataFrame({
    "Data": ["15/09/25", "10/09/25"],
    "Tipo": ["Geração", "Venda"],
    "Quantidade": ["50 créditos", "30 créditos"],
    "Valor": ["R$ 25,00", "R$ 15,00"]
})
st.table(historico)

st.markdown("---")

# -------------------------
# Botões de ação (alinhados, mesmo tamanho)
# -------------------------
st.markdown("### Ações rápidas")

# CSS para alinhar e uniformizar os botões
st.markdown(
    """
    <style>
    .action-btn {
        display: inline-block;
        width: 100%;
        padding: 12px;
        border-radius: 8px;
        font-weight: 600;
        text-align: center;
        border: none;
        cursor: pointer;
        margin-top: 5px;
        margin-bottom: 5px;
    }
    .green { background-color: #2ECC71; color: white; }
    .orange { background-color: #E67E22; color: white; }
    .blue { background-color: #3498DB; color: white; }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<button class="action-btn green">Carregar veículo</button>', unsafe_allow_html=True)
with col2:
    st.markdown('<button class="action-btn orange">Vender créditos</button>', unsafe_allow_html=True)
with col3:
    st.markdown('<button class="action-btn blue">Ver NFT</button>', unsafe_allow_html=True)
