import streamlit as st
import pandas as pd
import plotly.express as px

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
        options_nivel1 = st.multiselect(
            "Selecione as categorias (Nível 1)",
            df['Nível 1'].unique(),
        )
        if options_nivel1:
            filtered_df = df[df['Nível 1'].isin(options_nivel1)]  # Faz a filtragem
            st.write("Você selecionou", len(options_nivel1), "categorias")
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
        options_nivel1 = st.multiselect(
            "Selecione as categorias (Nível 1)",
            df['Nível 1'].unique(),
        )
        if options_nivel1:
            filtered_df = df[df['Nível 1'].isin(options_nivel1)]  # Faz a filtragem
            if 'Nível 3' in filtered_df.columns:
                options_nivel3 = st.multiselect(
                    "Selecione as subcategorias (Nível 3)",
                    filtered_df['Nível 3'].unique(),
                )
                if options_nivel3:
                    filtered_df = filtered_df[filtered_df['Nível 3'].isin(options_nivel3)]  # Faz a filtragem
                    st.write("Você selecionou", len(options_nivel1), "categorias e", len(options_nivel3), "subcategorias")
                    
                    # Selecionar a coluna para análise
                    column = st.selectbox("Selecione a coluna para análise", filtered_df.columns)
                    
                    if column in filtered_df.columns:
                        # Exemplo de gráfico de barras usando plotly
                        st.subheader("Gráfico de Barras")
                        fig = px.bar(filtered_df, x='Nível 1', y=column, color='Nível 3', title=f"Gráfico de Barras - {column}", barmode='group')
                        st.plotly_chart(fig)
                        
                        # Exemplo de gráfico de pizza usando plotly
                        st.subheader("Gráfico de Pizza")
                        fig = px.pie(filtered_df, names='Nível 3',values=column, title=f"Gráfico de Pizza - {column}")
                        st.plotly_chart(fig)
                        
                        # Exemplo de gráfico de área usando plotly
                        st.subheader("Gráfico de Área")
                        fig = px.area(filtered_df, x='Nível 3', y=column, color='Nível 3', title=f"Gráfico de Área - {column}")
                        st.plotly_chart(fig)
                    else:
                        st.write(f"A coluna '{column}' não existe no DataFrame.")
                else:
                    st.write("Nenhuma subcategoria selecionada")
            else:
                st.write("A coluna 'Nível 3' não existe no DataFrame.")
        else:
            st.write("Nenhuma categoria selecionada")
    else:
        st.write("A coluna 'Nível 1' não existe no DataFrame.")


