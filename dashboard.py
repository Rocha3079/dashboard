import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Share das Categorias")
st.write("Filial de Bento Gonçalves")

st.markdown("Tabela de Dados")
try:
    df = pd.read_excel(r"C:\Users\lucas.fachi\Desktop\NICOLAS - GC\PYTHON\base_teste.xlsx")
    st.table(df)
except:
    st.write("Erro ao carregar a base de dados")
    st.stop()
