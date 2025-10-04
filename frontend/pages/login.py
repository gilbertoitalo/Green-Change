import streamlit as st
import sqlite3, pathlib
import hashlib

# DB em frontend/data (fora do versionamento)
DATA_DIR = pathlib.Path(__file__).resolve().parents[1] / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = DATA_DIR / "users.db"

# uma única conexão
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()

st.set_page_config(page_title="Login / Cadastro", layout="wide")

# cria tabela se não existir
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
""")
conn.commit()

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def check_login(username: str, password: str) -> bool:
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    row = c.fetchone()
    return bool(row and row[0] == hash_password(password))

def register_user(username: str, password: str) -> bool:
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                  (username, hash_password(password)))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

# UI
if "show_signup" not in st.session_state:
    st.session_state.show_signup = False

if not st.session_state.show_signup:
    with st.form("login_form"):
        st.subheader("Login")
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        if st.form_submit_button("Entrar"):
            if check_login(username, password):
                st.success(f"Bem-vindo, {username}!")
            else:
                st.error("Usuário ou senha incorretos.")
    if st.button("Não possui cadastro? Clique aqui para se cadastrar"):
        st.session_state.show_signup = True
else:
    st.subheader("Cadastro de Usuário")
    with st.form("signup_form"):
        new_user = st.text_input("Escolha um nome de usuário")
        new_password = st.text_input("Escolha uma senha", type="password")
        confirm_password = st.text_input("Confirme a senha", type="password")
        if st.form_submit_button("Cadastrar"):
            if new_password != confirm_password:
                st.error("As senhas não coincidem.")
            elif register_user(new_user, new_password):
                st.success("Cadastro realizado! Volte ao login.")
                st.session_state.show_signup = False
            else:
                st.error("Usuário já existe. Escolha outro nome.")
    if st.button("Voltar ao login"):
        st.session_state.show_signup = False
