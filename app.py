import streamlit as st
import json
import pandas as pd
from datetime import datetime
from modules.ai_client import get_ai_response
from modules.data_loader import load_all_data
from modules.dashboard import render_dashboard
from modules.chat import render_chat

st.set_page_config(
    page_title="FinBot — Assistente Financeiro IA",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    .main-header h1 { color: #e2b96f; margin: 0; font-size: 2.2rem; }
    .main-header p  { color: #a0aec0; margin: 0.5rem 0 0; }

    .metric-card {
        background: #1e2a3a;
        border: 1px solid #2d3748;
        border-radius: 10px;
        padding: 1.2rem;
        text-align: center;
    }
    .metric-card .label { color: #a0aec0; font-size: 0.85rem; margin-bottom: 0.3rem; }
    .metric-card .value { color: #e2b96f; font-size: 1.6rem; font-weight: bold; }

    .chat-message-user {
        background: #2d3748;
        border-radius: 10px 10px 2px 10px;
        padding: 0.8rem 1rem;
        margin: 0.5rem 0;
        color: #e2e8f0;
    }
    .chat-message-bot {
        background: #1a2a3a;
        border-left: 3px solid #e2b96f;
        border-radius: 2px 10px 10px 10px;
        padding: 0.8rem 1rem;
        margin: 0.5rem 0;
        color: #e2e8f0;
    }
    .sidebar .sidebar-content { background: #1a1a2e; }
    div[data-testid="stSidebar"] { background: #1a1a2e; }
</style>
""", unsafe_allow_html=True)

# ── Header ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <h1>💰 FinBot — Assistente Financeiro IA</h1>
    <p>Seu consultor financeiro pessoal, disponível 24h</p>
</div>
""", unsafe_allow_html=True)

# ── Load data ────────────────────────────────────────────────────────────────
data = load_all_data()

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 👤 Perfil do Investidor")
    perfil = data["perfil"]
    st.markdown(f"**Nome:** {perfil['nome']}")
    st.markdown(f"**Idade:** {perfil['idade']} anos")
    st.markdown(f"**Profissão:** {perfil['profissao']}")
    st.markdown(f"**Perfil:** {perfil['perfil_investidor'].capitalize()}")
    st.markdown(f"**Renda Mensal:** R$ {perfil['renda_mensal']:,.2f}")
    st.markdown("---")

    st.markdown("### ⚙️ Configuração da IA")
    ai_provider = st.selectbox(
        "Provedor de IA",
        ["Groq (Rápido - Recomendado)", "Ollama (Local)"],
        help="Groq é gratuito e muito mais rápido que rodar localmente."
    )
    if "Groq" in ai_provider:
        groq_key = st.text_input(
            "Groq API Key",
            type="password",
            help="Obtenha grátis em console.groq.com"
        )
        st.session_state["groq_key"] = groq_key
        st.session_state["ai_provider"] = "groq"
        st.markdown("[🔑 Obter chave gratuita](https://console.groq.com)", unsafe_allow_html=False)
    else:
        ollama_model = st.text_input("Modelo Ollama", value="llama3.2", help="Ex: llama3.2, mistral, phi3")
        st.session_state["ollama_model"] = ollama_model
        st.session_state["ai_provider"] = "ollama"

    st.markdown("---")
    if st.button("🗑️ Limpar conversa", use_container_width=True):
        st.session_state["messages"] = []
        st.rerun()

# ── Tabs ─────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["💬 Chat Financeiro", "📊 Dashboard", "📚 Produtos & FAQ"])

with tab1:
    render_chat(data)

with tab2:
    render_dashboard(data)

with tab3:
    from modules.produtos import render_produtos
    render_produtos(data)
