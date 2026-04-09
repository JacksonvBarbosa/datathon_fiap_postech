import streamlit as st
import joblib
import numpy as np

# Configuração da página
st.set_page_config(
    page_title="Risco de Defasagem",
    page_icon="🎓",
    layout="centered"
)

# Carregar modelo
modelo = joblib.load("modelo_risco.pkl")

# Título
st.title("🎓 Previsão de Risco de Defasagem Escolar")

st.markdown(
"""
Este modelo estima a **probabilidade de um aluno entrar em risco de defasagem**
com base em indicadores acadêmicos e de engajamento.
"""
)

st.divider()

st.subheader("📊 Indicadores do aluno")

# Layout em colunas
col1, col2 = st.columns(2)

with col1:
    ian_2022 = st.number_input("IAN 2022", 0.0, 10.0, step=0.1)
    ida_2022 = st.number_input("IDA 2022", 0.0, 10.0, step=0.1)
    ieg_2022 = st.number_input("IEG 2022", 0.0, 10.0, step=0.1)

with col2:
    ipv_2022 = st.number_input("IPV 2022", 0.0, 10.0, step=0.1)
    delta_ida_22_23 = st.number_input("Δ IDA 22 → 23", step=0.1)
    delta_ieg_22_23 = st.number_input("Δ IEG 22 → 23", step=0.1)

media_ian_ate_23 = st.number_input("Média IAN até 2023", 0.0, 10.0, step=0.1)

st.divider()

# Botão
if st.button("🔎 Calcular risco", use_container_width=True):

    dados = np.array([[ 
        ian_2022,
        ida_2022,
        ieg_2022,
        ipv_2022,
        delta_ida_22_23,
        delta_ieg_22_23,
        media_ian_ate_23
    ]])

    probabilidade = modelo.predict_proba(dados)[0][1]

    st.subheader("Resultado da previsão")

    # Barra visual
    st.progress(probabilidade)

    st.metric(
        label="Probabilidade de risco",
        value=f"{probabilidade:.2%}"
    )

    st.divider()

    # Classificação de risco
    if probabilidade >= 0.28:
        st.error("⚠️ **Aluno com risco elevado de defasagem**")
        st.write(
        """
        Recomenda-se acompanhamento pedagógico e monitoramento
        do desempenho e engajamento do aluno.
        """
        )
    else:
        st.success("✅ **Baixo risco de defasagem**")
        st.write(
        """
        O aluno apresenta baixo risco de aumento de defasagem
        com base nos indicadores atuais.
        """
        )

st.divider()

st.caption("Modelo preditivo baseado em indicadores educacionais (IDA, IEG, IAN e IPV).")