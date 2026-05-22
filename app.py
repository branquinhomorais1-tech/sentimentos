import nltk


nltk.download('punkt_tab')

palavra = "python é dhr"

tokens = nltk.word_tokenize(palavra)

print(tokens)

nltk.download('averaed_percetron_tagger_eng')

tagged = nltk.pos_tag(tokens)

print(tagged)
#-------------------------------------------------------------------------

import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Garante o download do dicionário do VADER necessário para a análise
@st.cache_resource
def download_nltk_resources():
    nltk.download('vader_lexicon')

download_nltk_resources()

# Inicializa o analisador de sentimentos
sia = SentimentIntensityAnalyzer()

# Configuração da interface do Streamlit
st.title("Analisador de Sentimentos Simples")
st.write("Digite uma frase (de preferência em inglês) para descobrir o sentimento dela.")

# 1. O Prompt (Input de texto)
user_input = st.text_input("Sua frase:", placeholder="Type something here...")

# 2. O Botão para dar Run
if st.button("Analisar Sentimento"):
    if user_input.strip() != "":
        # Processamento do sentimento
        scores = sia.polarity_scores(user_input)
        compound = scores['compound']
        
        # Classificação simples baseada no score do VADER
        if compound >= 0.05:
            resultado = "😊 Positivo"
        elif compound <= -0.05:
            resultado = "😡 Negativo"
        else:
            resultado = "😐 Neutro"
            
        # 3. O st.write() para mostrar o resultado
        st.write(f"O sentimento predominante é: **{resultado}**")
        st.write(f"Pontuação detalhada: {scores}")
    else:
        st.write("⚠️ Por favor, digite alguma frase antes de analisar.")
#--------------------------------------------------------------
        