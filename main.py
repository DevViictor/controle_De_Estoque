import streamlit as st
import pandas as pd

janela = st.sidebar.radio("Home",["Inicio"])

arquivo = st.file_uploader("Carregue a planilha do sap",type=["ods","xlsx"])

st.header("Controle de Estoque")

if arquivo is not None:
    leitor = pd.read_excel(arquivo)

    st.dataframe(leitor)


