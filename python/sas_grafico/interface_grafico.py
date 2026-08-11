import streamlit as st
import pandas as pd

# titulo
st.title("Criador de Gráficos com SAS")

#local de upload de arquivos
upload_file = st.file_uploader("Escolha um arquivo", type=["csv", "xlsx"])

#seleão de colunas
df = pd.DataFrame()
if upload_file is not None:
    if upload_file.name.endswith(".csv"):
        df = pd.read_csv(upload_file)
    else:
        df = pd.read_excel(upload_file)
    



#tipo de gráfico
tipo_grafico = st.sidebar.selectbox("Tipo de gráfico",
 ["Selecione", "Barra", "Linha", "Dispersão"]
 )

colunas_para_grafico = st.sidebar.multiselect(
    "Selecione as colunas para o gráfico",
    df.columns
    )

#gráfico
if tipo_grafico == "Barra":
    st.bar_chart(df[colunas_para_grafico])
elif tipo_grafico == "Linha":
    st.line_chart(df[colunas_para_grafico])
elif tipo_grafico == "Dispersão":
    st.scatter_chart(df[colunas_para_grafico])
