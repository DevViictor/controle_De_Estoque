import streamlit as st
import pandas as pd


arquivo = st.file_uploader("Carregue a planilha do sap",type="xlsx")

st.header("Controle de Estoque")

if arquivo is not None:
    leitor = pd.read_excel(arquivo)

    st.dataframe(leitor)


