import streamlit as st
import pandas as pd

st.sidebar.header("Seu estoque")
janela = st.sidebar.radio("",["Inicio"])

arquivo = st.file_uploader("Carregue a planilha do sap",type=["ods","xlsx"])

st.header("Controle de Estoque")

if arquivo is not None:
    leitor = pd.read_excel(arquivo)

    st.dataframe(leitor)


