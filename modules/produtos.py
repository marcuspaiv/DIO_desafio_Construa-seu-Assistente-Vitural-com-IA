import streamlit as st

FAQS = [
    {
        "pergunta": "O que é Tesouro Selic e para que serve?",
        "resposta": (
            "O **Tesouro Selic** é um título público federal atrelado à taxa Selic. "
            "É considerado o investimento mais seguro do Brasil e ideal para a **reserva de emergência**, "
            "pois tem liquidez diária — você pode resgatar a qualquer momento sem perder rendimento. "
            "Aporte mínimo de R$ 30,00."
        ),
    },
    {
        "pergunta": "Qual a diferença entre CDB e LCI/LCA?",
        "resposta": (
            "**CDB** (Certificado de Depósito Bancário) é tributado pelo IR regressivo. "
            "**LCI/LCA** (Letras de Crédito Imobiliário/Agrícola) são **isentas de IR** para pessoa física, "
            "mas geralmente exigem prazo de carência (mínimo 90 dias). "
            "Para reserva de emergência, prefira CDB com liquidez diária."
        ),
    },
    {
        "pergunta": "O que são FIIs (Fundos de Investimento Imobiliário)?",
        "resposta": (
            "FIIs são fundos que investem em imóveis ou papéis imobiliários. "
            "Eles distribuem **dividendos mensais isentos de IR** e são negociados na bolsa como ações. "
            "O Dividend Yield médio fica entre 6% e 12% ao ano. "
            "Indicados para perfil moderado que busca renda passiva recorrente."
        ),
    },
    {
        "pergunta": "Quanto devo ter na reserva de emergência?",
        "resposta": (
            "A recomendação geral é ter entre **3 a 6 meses** de despesas mensais. "
            "Para profissionais CLT, 3 meses costuma ser suficiente. "
            "Para autônomos e empreendedores, recomenda-se 6 meses. "
            "O ideal é manter esse valor no **Tesouro Selic ou CDB com liquidez diária**."
        ),
    },
    {
        "pergunta": "Como começar a investir com pouco dinheiro?",
        "resposta": (
            "1. Monte sua **reserva de emergência** primeiro (Tesouro Selic).\n"
            "2. Depois explore **CDB** e **LCI/LCA** para médio prazo.\n"
            "3. Com mais experiência, diversifique com **FIIs** para renda passiva.\n"
            "4. Ações e fundos de ações só para quem aceita volatilidade e pensa no longo prazo.\n\n"
            "Comece com pequenos aportes mensais e seja consistente!"
        ),
    },
]


RISCO_COLOR = {"baixo": "🟢", "medio": "🟡", "alto": "🔴"}


def render_produtos(data: dict):
    produtos = data["produtos"]
    perfil   = data["perfil"]

    st.markdown("### 🏦 Produtos Financeiros Disponíveis")
    st.markdown(
        f"Recomendações baseadas no seu perfil: **{perfil['perfil_investidor'].capitalize()}** "
        f"| Aceita risco: **{'Sim' if perfil['aceita_risco'] else 'Não'}**"
    )
    st.markdown("---")

    cols = st.columns(2)
    for i, produto in enumerate(produtos):
        with cols[i % 2]:
            risco_icon = RISCO_COLOR.get(produto["risco"], "⚪")
            indicado = perfil["perfil_investidor"] in produto["indicado_para"].lower() or \
                       produto["risco"] == "baixo"

            badge = "✅ **Indicado para você**" if indicado else "⚠️ Fora do seu perfil"

            with st.expander(f"{risco_icon} {produto['nome']}", expanded=indicado):
                st.markdown(f"**Categoria:** {produto['categoria'].replace('_', ' ').title()}")
                st.markdown(f"**Risco:** {risco_icon} {produto['risco'].capitalize()}")
                st.markdown(f"**Rentabilidade:** {produto['rentabilidade']}")
                st.markdown(f"**Aporte mínimo:** R$ {produto['aporte_minimo']:,.2f}")
                st.markdown(f"**Indicado para:** {produto['indicado_para']}")
                st.markdown(f"{badge}")

    st.markdown("---")
    st.markdown("### ❓ Perguntas Frequentes")

    for faq in FAQS:
        with st.expander(f"❓ {faq['pergunta']}"):
            st.markdown(faq["resposta"])
