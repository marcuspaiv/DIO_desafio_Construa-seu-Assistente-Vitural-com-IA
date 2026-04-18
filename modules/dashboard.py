import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def render_dashboard(data: dict):
    perfil     = data["perfil"]
    transacoes = data["transacoes"]

    # ── KPI Cards ────────────────────────────────────────────────────────────
    st.markdown("### 📊 Visão Geral Financeira")
    col1, col2, col3, col4 = st.columns(4)

    reserva_atual    = perfil["reserva_emergencia_atual"]
    reserva_objetivo = 15000.0
    progresso        = (reserva_atual / reserva_objetivo) * 100

    with col1:
        st.metric("💰 Patrimônio Total", f"R$ {perfil['patrimonio_total']:,.2f}")
    with col2:
        st.metric("📅 Renda Mensal", f"R$ {perfil['renda_mensal']:,.2f}")
    with col3:
        st.metric("🛡️ Reserva de Emergência", f"R$ {reserva_atual:,.2f}",
                  delta=f"{progresso:.1f}% da meta")
    with col4:
        faltam = reserva_objetivo - reserva_atual
        st.metric("🎯 Falta para a Reserva", f"R$ {faltam:,.2f}")

    st.markdown("---")

    # ── Reserva de emergência ─────────────────────────────────────────────────
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("#### 🛡️ Progresso da Reserva de Emergência")
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=progresso,
            delta={"reference": 100, "suffix": "%"},
            number={"suffix": "%", "font": {"size": 32}},
            gauge={
                "axis": {"range": [0, 100]},
                "bar":  {"color": "#e2b96f"},
                "steps": [
                    {"range": [0, 33],  "color": "#2d1b1b"},
                    {"range": [33, 66], "color": "#2d2a1b"},
                    {"range": [66, 100],"color": "#1b2d1b"},
                ],
                "threshold": {
                    "line": {"color": "#48bb78", "width": 4},
                    "thickness": 0.75,
                    "value": 100,
                },
            },
            title={"text": f"R$ {reserva_atual:,.0f} / R$ {reserva_objetivo:,.0f}"},
        ))
        fig_gauge.update_layout(
            height=300,
            paper_bgcolor="rgba(0,0,0,0)",
            font={"color": "#e2e8f0"},
        )
        st.plotly_chart(fig_gauge, use_container_width=True)

    with col_right:
        st.markdown("#### 🎯 Metas Financeiras")
        metas = perfil.get("metas", [])
        if metas:
            patrimonio = perfil["patrimonio_total"]
            meta_labels  = [m["meta"] for m in metas]
            meta_valores = [m["valor_necessario"] for m in metas]
            meta_atual   = [min(patrimonio, v) for v in meta_valores]
            meta_falta   = [max(0, v - patrimonio) for v in meta_valores]

            fig_metas = go.Figure()
            fig_metas.add_trace(go.Bar(
                name="Conquistado", x=meta_labels, y=meta_atual,
                marker_color="#e2b96f",
            ))
            fig_metas.add_trace(go.Bar(
                name="Falta", x=meta_labels, y=meta_falta,
                marker_color="#2d3748",
            ))
            fig_metas.update_layout(
                barmode="stack",
                height=300,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font={"color": "#e2e8f0"},
                legend={"orientation": "h", "y": -0.2},
                yaxis={"title": "R$", "gridcolor": "#2d3748"},
            )
            st.plotly_chart(fig_metas, use_container_width=True)

    st.markdown("---")

    # ── Transações ───────────────────────────────────────────────────────────
    st.markdown("#### 💳 Análise de Transações")

    if not transacoes.empty:
        # Tenta detectar colunas de categoria e valor
        cat_col = next((c for c in transacoes.columns if "categ" in c.lower()), None)
        val_col = next((c for c in transacoes.columns if "valor" in c.lower() or "value" in c.lower()), None)
        dat_col = next((c for c in transacoes.columns if "data" in c.lower() or "date" in c.lower()), None)

        col_a, col_b = st.columns(2)

        with col_a:
            if cat_col and val_col:
                gastos_cat = transacoes.groupby(cat_col)[val_col].sum().reset_index()
                gastos_cat.columns = ["Categoria", "Total"]
                fig_pie = px.pie(
                    gastos_cat, values="Total", names="Categoria",
                    title="Gastos por Categoria",
                    color_discrete_sequence=px.colors.sequential.YlOrBr,
                    hole=0.4,
                )
                fig_pie.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    font={"color": "#e2e8f0"},
                    height=320,
                )
                st.plotly_chart(fig_pie, use_container_width=True)
            else:
                st.info("Coluna de categoria ou valor não encontrada no CSV.")

        with col_b:
            if dat_col and val_col:
                transacoes[dat_col] = pd.to_datetime(transacoes[dat_col], errors="coerce")
                tx_tempo = transacoes.dropna(subset=[dat_col]).sort_values(dat_col)
                tx_tempo["mes"] = tx_tempo[dat_col].dt.to_period("M").astype(str)
                tx_mes = tx_tempo.groupby("mes")[val_col].sum().reset_index()
                fig_bar = px.bar(
                    tx_mes, x="mes", y=val_col,
                    title="Gastos por Mês",
                    color_discrete_sequence=["#e2b96f"],
                )
                fig_bar.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font={"color": "#e2e8f0"},
                    height=320,
                    xaxis={"gridcolor": "#2d3748"},
                    yaxis={"gridcolor": "#2d3748", "title": "R$"},
                )
                st.plotly_chart(fig_bar, use_container_width=True)
            else:
                st.info("Coluna de data ou valor não encontrada no CSV.")

        st.markdown("#### 📋 Últimas Transações")
        st.dataframe(
            transacoes.tail(10),
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("Nenhuma transação encontrada.")
