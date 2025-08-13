import streamlit as st
import pandas as pd


st.sidebar.header("Controle de Estoque")
janela = st.sidebar.radio("", ["Filtro"])

coluns = ["Material","Texto breve material","Nº de série"]

arquivo = st.file_uploader("Carregue a planilha desejada",type=["ods","xlsx"])

st.header("Controle de Estoque")

if arquivo is not None:
    filtro = st.text_input("Digite o material ou N° de série que deseja encontrar")
    leitor = pd.read_excel(arquivo,usecols=coluns)
    
    #aplica a condição de filtro digitada pelo usuario e aplica na planilha 
    if filtro:
        newleitor = leitor[leitor["Nº de série"].astype(str).str.contains(filtro, case=False, na=False)] 

newleitor = leitor[leitor["Material"].astype(str).str.contains(filtro, case=False, na=False)]
      
    else:
        newleitor = leitor

    quantidade_material = len(newleitor) 
    st.write("Total de produtos",quantidade_material)
    st.dataframe(newleitor)
    
