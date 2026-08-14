# importa bibliotecas necessárias para execução da aplicação
import streamlit as st
import pandas as pd
import joblib

# importa o modelo
@st.cache_resource # armazena o modelo na memória cache do servidor
def carregar_modelo(): # cria função para carregar modelo (a sintaxe do @st.cache_resource exige que este seja colocado sobre funções ou classes)
    return joblib.load('modelo_randomforest_usinagem.pkl') # retorna o carregamento do modelo em .pkl

modelo = carregar_modelo() # execulta função carrega_modelo()

# configura cabeçalho da página
st.set_page_config(page_title='Vida útil de ferramenta', layout='centered') # define configurações principais da página
st.title('Vida útil de ferramenta - Fresa HOB') # define um título a ser exibido na página
st.markdown('Insira os dados abaixo para estimar a vida útil ideal da ferramenta para troca preventiva') # define um texto de apresentação a ser exibido

# configura campos de entrada de dados da página
st.subheader('Dados de processo') # define um subtítulo para esta seção
col1, col2 = st.columns(2) # define uma estrutura com duas colunas para os campos de entrada de dados

