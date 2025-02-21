import streamlit as st
import pandas as pd
import numpy as np

# Função para formatar porcentagem
def format_percentage(val):
    """Formats a value as percentage with 2 decimal places."""
    return "{:.2f}%".format(val * 100)

# Carregar os dados
try:
    df = pd.read_excel('base_teste.xlsx')
    # Identifica as colunas que contêm porcentagens
    percentage_cols = [col for col in df.columns if '%' in col]

    # Aplica o formato nessas colunas
    for col in percentage_cols:
        if df[col].dtype == 'float64' or df[col].dtype == 'int64':  # Checa se a coluna é numérica
            df[col] = df[col].apply(format_percentage)

except Exception as e:
    st.write("Erro ao carregar a base de dados:", e)
    st.stop()

# Menu de navegação na barra lateral
page = st.sidebar.selectbox("Selecione a página", ["Base de dados 🗂️", "Gráficos 📊"])

# Página 1: Base de dados
if page == "Base de dados 🗂️":
    st.title("Share das Categorias")
    st.markdown("Base de dados 🗂️")
    st.write("Filial de Bento Gonçalves")

    if 'Nível 1' in df.columns:
        options = st.multiselect(
            "Selecione as categorias",
            df['Nível 1'].unique(),
        )
        if options:
            filtered_df = df[df['Nível 1'].isin(options)]  # Faz a filtragem
            st.write("Você selecionou", len(options), "categorias")
            st.dataframe(filtered_df, use_container_width=True)
        else:
            st.write("Nenhuma categoria selecionada")
            st.dataframe(df, use_container_width=True)
    else:
        st.write("A coluna 'Nível 1' não existe no DataFrame.")
    st.write("Geral")
    st.dataframe(df, use_container_width=True)

# Página 2: Gráficos
elif page == "Gráficos 📊":
    st.title("Gráficos das Categorias")
    st.markdown("Gráficos 📊")

    if 'Nível 1' in df.columns:
        options = st.multiselect(
            "Selecione as categorias",
            df['Nível 1'].unique(),
        )
        if options:
            filtered_df = df[df['Nível 1'].isin(options)]  # Faz a filtragem
            st.write("Você selecionou", len(options), "categorias")
            st.dataframe(filtered_df, use_container_width=True)
        else:
            st.write("Nenhuma categoria selecionada")
            st.dataframe(df, use_container_width=True)
    else:
        st.write("A coluna 'Nível 1' não existe no DataFrame.")
