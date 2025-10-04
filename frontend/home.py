import streamlit as st
import os

# -------------------------------
# Configuração básica
# -------------------------------
st.set_page_config(page_title="GreenCharge", layout="wide")

# -------------------------------
# Simulação de login
# -------------------------------
if "user" not in st.session_state:
    st.session_state.user = None

# Função para logout
def logout():
    st.session_state.user = None

# -------------------------------
# Header com botão login 
# -------------------------------
col1, col2 = st.columns([9, 1])
with col1:
    st.markdown("")  
with col2:
    if st.session_state.user:
        # Botão de usuário logado com dropdown
        st.markdown(f"""
        <div style="position: relative; display: inline-block;">
            <button style="
                background-color:#31572c; color:white; border:none; 
                padding:8px 16px; border-radius:6px; cursor:pointer;">
                {st.session_state.user} ▼
            </button>
            <div style="
                display:none;
                position:absolute;
                background-color:white;
                min-width:100px;
                box-shadow:0px 8px 16px 0px rgba(0,0,0,0.2);
                z-index:1;
                border-radius:6px;
            " id="dropdown-content">
                <a href='#' onclick='window.parent.location.reload()' 
                   style='color:#31572c; padding:8px 12px; display:block; text-decoration:none;'>Deslogar</a>
            </div>
        </div>
        <script>
        const btn = document.querySelector("button");
        const menu = document.getElementById("dropdown-content");
        btn.onclick = () => {{
            menu.style.display = menu.style.display === "block" ? "none" : "block";
        }}
        </script>
        """, unsafe_allow_html=True)
    else:
        st.markdown('<a href="/login" style="text-decoration:none;"><button style="background:#31572c; color:white; border:none; padding:8px 16px; border-radius:6px; cursor:pointer;">Login</button></a>', unsafe_allow_html=True)
# -------------------------------
# CSS CUSTOMIZADO
# -------------------------------
st.markdown("""
<style>
/* Hero ocupa topo completo */
.hero {
    background: linear-gradient(rgba(49,87,44,0.85), rgba(0,0,0,0.5)),
    url('carregador-de-carro-eletrico-de-carregamento-close-up.jpg') center/cover no-repeat;
    color: white;
    text-align: center;
    padding: 180px 20px; /* aumenta altura */
    border-radius: 0; /* sem borda arredondada */
    margin-bottom: 3rem;
}

/* Hero texto */
.hero h1 { font-size: 3rem; font-weight: 700; margin-bottom: 1rem; }
.hero p { font-size: 1.3rem; line-height: 1.5; }

/* Botões */
.btn {
    display: inline-block;
    margin: 1rem 0.5rem 0 0.5rem;
    padding: 14px 30px;
    border-radius: 8px;
    font-weight: 600;
    text-decoration: none;
    transition: all .2s;
}
.btn-green {
    background: #31572c;
    color: white !important;
    text-decoration: none !important;
    border: none;
}
.btn-green:hover {background:#2a4a25; transform:scale(1.05);}
.btn-outline {
    border: 2px solid #31572c;
    color: #31572c !important;  /* força o verde */
    background: white;
    text-decoration: none !important; /* remove sublinhado */
    font-weight: 600;
}
.btn-outline:hover {
    background:#f0fdf4;
    transform:scale(1.05);
    text-decoration: none !important; /* garante que não volte no hover */
}

/* Cards */
.card {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: white;
    border: 1px solid #eee;
    border-radius: 12px;
    padding: 24px;
    text-align: center;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    transition: transform .2s, box-shadow .2s;
    height: 160px; /* altura fixa opcional */
    min-height: 140px; /* altura mínima para responsividade */
}
.card:hover {
    transform: scale(1.03);
    box-shadow: 0 6px 14px rgba(0,0,0,0.1);
}
.cards-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 20px;
}

/* Espaçamento entre sessões */
.section-space { margin-top: 5rem; margin-bottom: 3rem; }
</style>
""", unsafe_allow_html=True)


# -------------------------------
# HERO
# -------------------------------
st.markdown("""
<div class="hero">
    <h1>Transforme sua recarga em créditos de carbono</h1>
    <p>Cada recarga do seu veículo elétrico gera créditos de carbono.<br>
    Impacto positivo para o planeta, valor real para você.</p>
    <div>
        <a href="./login" class="btn btn-green">Cadastre-se grátis</a>
        <a href="./simulador" class="btn btn-outline">Calcule seu impacto</a>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# COMO FUNCIONA
# -------------------------------
st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)
st.subheader("Como funciona")

steps = [
    "Carregue seu veículo",
    "Calculamos CO₂ evitado",
    "Crédito gerado",
    "Revenda às empresas",
    "Ganhe recompensas",
]

cols = st.columns(len(steps))

for col, text in zip(cols, steps):
    with col:
        st.markdown(f"""
        <div class="card">
            <h4 style="margin-top:15px; color:#31572c;">{text}</h4>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------
# BENEFÍCIOS
# -------------------------------
st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)
st.subheader("Benefícios")

beneficios = [
    ("Democratização", "Qualquer pessoa pode participar do mercado de carbono."),
    ("Transparência", "Blockchain garante rastreabilidade e confiança."),
    ("Recompensa", "Ganhe ao transformar sua recarga em créditos."),
    ("Escalabilidade", "Funciona em qualquer mercado global."),
]

cols = st.columns(4)
for col, (title, desc) in zip(cols, beneficios):
    with col:
        st.markdown(f"""
        <div class="card" style="background:#31572c; color:white;">
            <h4>{title}</h4>
            <p style="font-size:0.9rem;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------
# IMPACTO
# -------------------------------
st.markdown("""
<div style="
    text-align:center; 
    padding:80px 20px; 
    margin:3rem 0;
    color:white; 
    border-radius:12px;
    background: linear-gradient(rgba(49,87,44,0.9), rgba(49,87,44,0.9)), 
    url('conservacao-ambiental-no-jardim-para-criancas.jpg') center/cover;">
    <h2>Impacto real</h2>
    <p style="margin-top:1rem; font-size:1.1rem;">
        Um carro a combustão emite cerca de <strong>180g de CO₂</strong> por km.<br>
        Ao rodar <strong>10.000 km/ano</strong> com um EV, você evita quase 
        <strong>2 toneladas de CO₂</strong>.
    </p>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# CTA FINAL
# -------------------------------
st.markdown("""
<div style="text-align:center; padding:60px 20px;">
    <h2 style="color:#31572c;">Pronto para começar?</h2>
    <p style="margin-top:10px; font-size:1rem; color:#444;">
        Cadastre-se agora e transforme sua recarga em impacto positivo para o planeta 🌱
    </p>
    <a href="/login" class="btn btn-green" style="margin-top:20px;">Quero participar</a>
</div>
""", unsafe_allow_html=True)
