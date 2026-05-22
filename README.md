import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
import plotly.express as px
from datetime import datetime

# 1. Configurações Iniciais e Downloads
st.set_page_config(page_title="Sentimento App & Admin", layout="wide")

@st.cache_resource
def download_nltk_resources():
    nltk.download('vader_lexicon')

download_nltk_resources()
sia = SentimentIntensityAnalyzer()

# 2. Simulação de Banco de Dados usando st.session_state
if "historico_db" not in st.session_state:
    # Iniciamos com alguns dados fictícios para o Admin não nascer vazio
    st.session_state.historico_db = pd.DataFrame([
        {"Data": "2026-05-20 10:00", "Texto": "I love this product!", "Sentimento": "😊 Positivo", "Score": 0.6369},
        {"Data": "2026-05-21 14:32", "Texto": "This is the worst service ever.", "Sentimento": "😡 Negativo", "Score": -0.6249},
        {"Data": "2026-05-22 09:15", "Texto": "Standard book, nothing special.", "Sentimento": "😐 Neutro", "Score": 0.0},
    ])

# 3. Criação das Abas (Interface Principal vs Admin)
aba_usuario, aba_admin = st.tabs(["🚀 Prompt do Usuário", "📊 Painel Admin (Edmim)"])

# ------------------------------------------------------------------------------
# ABA DO USUÁRIO
# ------------------------------------------------------------------------------
with aba_usuario:
    st.title("Analisador de Sentimentos")
    st.write("Digite uma frase em inglês para analisar.")

    user_input = st.text_input("Sua frase:", placeholder="Type something here...", key="user_text")

    if st.button("Analisar Sentimento", key="run_btn"):
        if user_input.strip() != "":
            # Análise com NLTK
            scores = sia.polarity_scores(user_input)
            compound = scores['compound']
            
            if compound >= 0.05:
                resultado = "😊 Positivo"
            elif compound <= -0.05:
                resultado = "😡 Negativo"
            else:
                resultado = "😐 Neutro"
                
            st.write(f"O sentimento predominante é: **{resultado}**")
            
            # Salva a análise no "Banco de Dados" (Session State)
            nova_linha = {
                "Data": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "Texto": user_input,
                "Sentimento": resultado,
                "Score": compound
            }
            # Atualiza o DataFrame na memória
            st.session_state.historico_db = pd.concat([
                st.session_state.historico_db, 
                pd.DataFrame([nova_linha])
            ], ignore_index=True)
            
            st.success("Análise salva no banco de dados com sucesso!")
        else:
            st.warning("Por favor, digite algo.")

# ------------------------------------------------------------------------------
# ABA ADMIN (EDMIM)
# ------------------------------------------------------------------------------
with aba_admin:
    st.title("🛡️ Painel de Administração")
    st.write("Visão geral de todas as análises realizadas no sistema.")
    
    df = st.session_state.historico_db

    # Módulo de Métricas (Key Performance Indicators)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Análises", len(df))
    with col2:
        total_positivos = len(df[df["Sentimento"] == "😊 Positivo"])
        st.metric("Total Positivos", total_positivos)
    with col3:
        score_medio = df["Score"].mean()
        st.metric("Score Médio Geral", f"{score_medio:.2f}")

    st.markdown("---")

    # Módulo de Gráficos e Tabelas
    col_grafico, col_tabela = st.columns([1, 1])

    with col_grafico:
        st.subheader("Distribuição dos Sentimentos")
        # Cria um gráfico de pizza interativo com Plotly
        fig = px.pie(df, names="Sentimento", color="Sentimento",
                     color_discrete_map={"😊 Positivo": "green", "😡 Negativo": "red", "😐 Neutro": "gray"})
        st.plotly_chart(fig, use_container_width=True)

    with col_tabela:
        st.subheader("Histórico de Logs (Banco de Dados)")
        # Mostra a tabela de dados completa, ordenada do mais recente para o mais antigo
        st.dataframe(df.iloc[::-1], use_container_width=True)

    # Botão para limpar os dados (Função útil de Admin)
    if st.button("Limpar Histórico de Logs"):
        st.session_state.historico_db = pd.DataFrame(columns=["Data", "Texto", "Sentimento", "Score"])
        st.rerun()
