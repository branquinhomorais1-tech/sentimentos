# 📊 Analisador de Sentimentos com Painel Admin

Uma aplicação web interativa desenvolvida em Python utilizando **Streamlit** e **NLTK (VADER)**. O projeto conta com duas interfaces centralizadas: um prompt para o usuário final analisar o sentimento de textos e um painel administrativo (Dashboard) para monitoramento de métricas e logs em tempo real.

---

## 🚀 Funcionalidades

* **Prompt de Usuário:** Input de texto simples para análise instantânea de sentimentos (Positivo, Negativo ou Neutro).
* **Processamento Natural (NLP):** Utilização do algoritmo VADER do `NLTK` para análise de polaridade.
* **Painel Admin (Dashboard):**
    * Métricas chave (KPIs) como total de análises e score médio geral.
    * Gráfico de pizza interativo gerado com `Plotly`.
    * Tabela de logs históricos para auditoria das análises realizadas.

---

## 🛠️ Tecnologias Utilizadas

* [Python](https://www.python.org/) (v3.9+)
* [Streamlit](https://streamlit.io/) (Interface Web)
* [NLTK](https://www.nltk.org/) (Processamento de Linguagem Natural)
* [Pandas](https://pandas.pydata.org/) (Manipulação de Dados)
* [Plotly](https://plotly.com/) (Gráficos Interativos)

---

## 💻 Como Rodar Localmente (VS Code)

Siga os passos abaixo para executar o projeto na sua máquina:

### 1. Clonar o Repositório
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio
