# importa bibliotecas necessárias para execução da aplicação
import streamlit as st
import pandas as pd
import joblib
import time

# importa o modelo
@st.cache_resource # armazena o modelo na memória cache do servidor
def carregar_modelo(): # cria função para carregar modelo (a sintaxe do @st.cache_resource exige que este seja colocado sobre funções ou classes)
    return joblib.load('modelo_randomforest_usinagem.pkl') # retorna o carregamento do modelo em .pkl

dicionario_modelo = carregar_modelo() # execulta função carrega_modelo()
modelo = dicionario_modelo['algoritmo'] # armazena o modelo em variável
margem_erro = dicionario_modelo['mae_otimizado'] # armazena o MAE em variável

# configura cabeçalho da página
st.set_page_config(page_title='Vida útil de ferramenta', layout='centered') # define configurações principais da página
st.logo('logo.png')
st.title('Vida útil de ferramenta - Fresa HOB') # define um título a ser exibido na página
st.markdown('Insira os dados abaixo para estimar a vida útil ideal da ferramenta para troca preventiva') # define um texto de apresentação a ser exibido

# configura campos de entrada de dados da página
st.subheader('Dados de processo') # define um subtítulo para esta seção
coluna1, coluna2 = st.columns(2) # define uma estrutura com duas colunas para os campos de entrada de dados

with coluna1: # campos de entrada de dados na primeira coluna
    avanco = st.selectbox('Avanço (mm/rev.)', [1.4, 1.5, 1.75, 2.0]) # selectbox para dado de 'Avanço'
    rpm = st.selectbox('Rotação (RPM)', [320, 350, 390, 510]) # selectbox para dado de 'Rotação'
    shifting = st.selectbox('Shifting (mm)', [10.0, 11.4]) # selectbox para dado de 'Shifting'

with coluna2: # campos de entrada de dados na segunda coluna
    revestimento = st.selectbox('Revestimento da ferramenta', ['Alcrona Pro', 'Alcrona Evo'])  # selectbox para dado de 'Revistimento'
    dureza_superficial = st.number_input('Dureza superficial (HRb)', min_value=80.0, max_value=120.0, value=95.0, step=0.5) # number_input para dados de 'dureza superficial'
    dureza_nucleo = st.number_input('Dureza do núcleo (HRb)', min_value=80.0, max_value=120.0, value=95.0, step=0.5) # number_input para dados de 'dureza do núcleo'

# cria botão para executar modelo
if st.button('Calcular ponto de troca preventiva', type='primary'):

    # converte o valor str da variável 'avanco' em valor numérico exigido pelo modelo
    if revestimento == 'Alcrona Pro': # compara variável 'revestimento' com texto 'Alcona Pro'
        revestimento_modelo = 1 # retorna '1' se verdadeiro
    else:
        revestimento_modelo = 0 # retorna '0' se falso

    # cria um df com o formato exato esperado pelo modelo
    dados_entrada = pd.DataFrame([{ # cria o df
        'Avanço mm/rev.': avanco, # insere em 'Avanço mm/rev.' os valores de 'avanco'
        'Rotação RPM': rpm, # insere em 'Rotação RPM' os valores de rpm
        'Shifting mm': shifting, # insere em 'Shifting mm' os valores de shifting
        'dureza sup': dureza_superficial, # insere em 'dureza sup' os valores de dureza_superficial
        'dureza nuc': dureza_nucleo, # insere em 'dureza nuc' os valores de dureza_nucleo
        'Revestimento_Alcrona Pro': revestimento_modelo # insere em 'Revestimento_Alcrona Pro' os valores de revestimento_modelo
    }])

    # exibe um título para a secção de resultado
    st.divider()
    st.subheader('Algorítmo de previsão de vida útil')

    # execulta uma espera enquanto 
    with st.spinner('Execultando modelo de Machine Learning'): # insere um elemento rotativo durante a espera
        time.sleep(3) # força o sistema a aguardar 3 segundos

        # execulta o modelo
        vida_util_estimada = modelo.predict(dados_entrada)[0] # armazena em vida_util_estimada o valor da previsão
        ponto_troca = int(vida_util_estimada - margem_erro) # armazena em variável o ponto ideal de traca preventiva da ferramenta

    # exibe o resultado
    st.success('Análise concluida') # exibe uma mensagem de conclusão
    st.metric(label='Troca preventiva recomendada em ', value=f'{ponto_troca} peças') # exibe uma mensagem com o ponto de troca recomendado
    st.caption(f'**Detalhes da validação:** Vida útil máxima teórica de {int(vida_util_estimada)} peças. Margem estática de segurança do modelo: -{int(margem_erro)} peças.') # exibe uma mensagem com detalhes do modelo

# rodapé com texto de autoria
rodape_css = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: transparent;
    color: #888888; /* Cor cinza para ficar bem discreto */
    text-align: center;
    font-size: 12px;
    padding: 10px;
    z-index: 100; /* Garante que fique por cima de outros elementos */
}
</style>
<div class="footer">Desenvolvido por Gabriel Santana</div>
"""

# O comando unsafe_allow_html=True permite que o Streamlit leia o CSS e o HTML
st.markdown(rodape_css, unsafe_allow_html=True)