import streamlit as st
from modules.ai_client import get_ai_response

QUICK_QUESTIONS = [
    "💰 Quanto falta para minha reserva de emergência?",
    "📈 Qual produto me recomenda agora?",
    "🏠 Estou no caminho certo para comprar o apartamento?",
    "📊 Como está meu progresso financeiro?",
    "🛡️ O que é Tesouro Selic e como funciona?",
    "💡 Como posso aumentar minha renda?",
]

def render_chat(data: dict):
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Boas-vindas
    if not st.session_state["messages"]:
        perfil = data["perfil"]
        st.info(
            f"👋 Olá, **{perfil['nome']}**! Sou o **FinBot**, seu assistente financeiro pessoal. "
            f"Estou aqui para te ajudar a alcançar suas metas financeiras. "
            f"Pode me perguntar sobre investimentos, sua reserva de emergência, produtos financeiros e muito mais!"
        )

    # Perguntas rápidas
    st.markdown("#### ⚡ Perguntas Rápidas")
    cols = st.columns(3)
    for i, question in enumerate(QUICK_QUESTIONS):
        with cols[i % 3]:
            if st.button(question, key=f"quick_{i}", use_container_width=True):
                _process_message(question, data)

    st.markdown("---")

    # Histórico
    st.markdown("#### 💬 Conversa")
    for msg in st.session_state["messages"]:
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.markdown(msg["content"])
        else:
            with st.chat_message("assistant", avatar="💰"):
                st.markdown(msg["content"])

    # Input
    if prompt := st.chat_input("Digite sua pergunta sobre finanças..."):
        _process_message(prompt, data)


def _process_message(prompt: str, data: dict):
    st.session_state["messages"].append({"role": "user", "content": prompt})

    with st.spinner("🤔 Analisando seu perfil financeiro..."):
        response = get_ai_response(prompt, data)

    st.session_state["messages"].append({"role": "assistant", "content": response})
    st.rerun()
