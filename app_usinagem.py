import streamlit as st
import pandas as pd
import joblib

# 1. Carregar o modelo treinado
@st.cache_resource # O cache evita que o app carregue o modelo do zero a cada clique
def carregar_modelo():
    return joblib.load('modelo_randomforest_usinagem.pkl')

modelo = carregar_modelo()

# 2. Configurações da Página
st.set_page_config(page_title="Ponto de Controle - Fresa HOB", layout="centered")
st.title("⚙️ Ponto de Controle: Vida Útil da Fresa HOB")
st.markdown("Insira os parâmetros de setup abaixo para estimar o limite seguro de peças antes da troca da ferramenta.")

# 3. Criar a Interface de Entrada de Dados (Inputs do Operador)
st.subheader("Parâmetros do Processo")
col1, col2 = st.columns(2)

with col1:
    avanco = st.selectbox("Avanço (mm/rev.)", [1.4, 1.5, 1.75, 2.0])
    rpm = st.selectbox("Rotação (RPM)", [320, 350, 390, 510])
    shifting = st.selectbox("Shifting (mm)", [10.0, 11.4])

with col2:
    revestimento = st.selectbox("Revestimento da Ferramenta", ["Alcrona Pro", "Alcrona Evo"])
    dureza_sup = st.number_input("Dureza Superficial Medida", min_value=85.0, max_value=110.0, value=95.0, step=0.5)
    dureza_nuc = st.number_input("Dureza do Núcleo Medida", min_value=85.0, max_value=110.0, value=94.0, step=0.5)

# 4. Botão de Cálculo
if st.button("Calcular Ponto de Troca", type="primary"):
    
    # Prepara o dado do revestimento (O modelo espera a coluna 'Revestimento_Alcrona Pro' com 0 ou 1)
    revest_pro = 1 if revestimento == "Alcrona Pro" else 0
    
    # Cria a matriz exatamente como o modelo aprendeu no Notebook
    dados_entrada = pd.DataFrame([{
        'Avanço mm/rev.': avanco,
        'Rotação RPM': rpm,
        'Shifting mm': shifting,
        'dureza sup': dureza_sup,
        'dureza nuc': dureza_nuc,
        'Revestimento_Alcrona Pro': revest_pro
    }])
    
    # 5. Fazer a previsão matemática
    vida_estimada_exata = modelo.predict(dados_entrada)[0]
    
    # 6. Aplicar a Regra de Manutenção Preventiva (Descontando a margem de erro MAE do modelo)
    margem_erro_mae = 110
    ponto_troca_seguro = int(vida_estimada_exata - margem_erro_mae)
    
    # Exibir o resultado para o operador
    st.divider()
    st.subheader("Resultado da Simulação")
    
    # Caixa de destaque (Métrica)
    st.metric(label="🚨 Troca Preventiva Recomendada (Ponto Seguro)", value=f"{ponto_troca_seguro} peças")
    
    st.info(f"**Detalhes Técnicos:** O modelo previu uma vida útil máxima teórica de **{int(vida_estimada_exata)} peças**. Uma margem de segurança de {margem_erro_mae} peças foi aplicada automaticamente para evitar riscos de quebra.")