import streamlit as st
import sqlite3
import hashlib

# -----------------------------
# Configuração da página
# -----------------------------
st.set_page_config(page_title="Login / Cadastro", layout="wide")

# -----------------------------
# Banco de dados SQLite
# -----------------------------
conn = sqlite3.connect("users.db")
c = conn.cursor()

# Criar tabela de usuários se não existir
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
''')
conn.commit()

# -----------------------------
# Funções auxiliares
# -----------------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_login(username, password):
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    result = c.fetchone()
    if result and result[0] == hash_password(password):
        return True
    return False

def register_user(username, password):
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                  (username, hash_password(password)))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

# -----------------------------
# Página principal
# -----------------------------
if "show_signup" not in st.session_state:
    st.session_state.show_signup = False

# Alterna entre login e cadastro
if not st.session_state.show_signup:
    with st.form("login_form"):
        st.subheader("Login")
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        submitted = st.form_submit_button("Entrar")

        if submitted:
            if check_login(username, password):
                st.success(f"Bem-vindo, {username}!")
                st.write("Aqui vai o conteúdo protegido da aplicação.")
            else:
                st.error("Usuário ou senha incorretos.")

    if st.button("Não possui cadastro? Clique aqui para se cadastrar"):
        st.session_state.show_signup = True

    st.markdown(
        """
        <style>
        div.stButton > button:first-child {
            background-color: #A9A9A9;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True
    )

else:
    st.subheader("Cadastro de Usuário")
    with st.form("signup_form"):
        new_user = st.text_input("Escolha um nome de usuário")
        new_password = st.text_input("Escolha uma senha", type="password")
        confirm_password = st.text_input("Confirme a senha", type="password")
        registered = st.form_submit_button("Cadastrar")

        if registered:
            if new_password != confirm_password:
                st.error("As senhas não coincidem.")
            elif register_user(new_user, new_password):
                st.success("Cadastro realizado com sucesso! Volte ao login.")
                st.session_state.show_signup = False
            else:
                st.error("Usuário já existe. Escolha outro nome.")
    
    if st.button("Voltar ao login"):
        st.session_state.show_signup = False
