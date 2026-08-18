# Ponto de Controle: Vida Útil da Fresa HOB

## Sobre o Projeto
Este projeto desenvolve uma aplicação web focada na troca preventiva de ferramentas de usinagem de fresas HOB. O objetivo é estimar a vida útil ideal de uma ferramenta de usinagem para que o operador possa realizar a troca preventiva de forma segura, evitando quebras e sucatas de peças fabricadas com defeitos. 

A aplicação utiliza um modelo de **Machine Learning** que cruza parâmetros de corte, geometria e propriedades do material para determinar o ponto exato de troca e foi disponibilizada no link abaixo para acesso público.

[Aplicação para previsão de vida útil de ferramenta](https://hobtoollife.streamlit.app/)

## Estrutura do Repositório
* **`app_vida_util.py`**: Arquivo principal que executa a interface web do sistema utilizando o framework Streamlit.
* **`modelagem_hob.ipynb`**: Notebook Jupyter contendo todo o pipeline de  de dados, desde a limpeza e Análise Exploratória (EDA) até o treinamento e otimização do algoritmo.
* **`modelo_randomforest_usinagem.pkl`**: Pacote exportado contendo o modelo matemático treinado e suas métricas de validação (como o MAE usado como margem de segurança).
* **`requirements.txt`**: Lista com as versões exatas de todas as bibliotecas necessárias para rodar o projeto.
* **`logo.png`**: Imagem com a identidade visual para interface do sistema.

## Tecnologias Utilizadas
O ambiente de desenvolvimento e produção foi construído com as seguintes especificações e bibliotecas:
* Windows 11 (versão 25H2)
* Python (versão 3.13.7)
* VS Code (versão 1.131.0)
* **Bibliotecas Principais:** Pandas, Scikit-learn, Plotly, Matplotlib, Seaborn, Streamlit e Joblib.

## Como Configurar e Executar o Projeto

Siga os passos abaixo para configurar o ambiente virtual no terminal do VS Code e rodar o aplicativo localmente:

1. Abra o VS Code no diretório do projeto e inicie o terminal (PowerShell).
2. Crie um ambiente virtual executando: `python -m venv .venv`.
3. Ative o ambiente virtual executando: `.\.venv\Scripts\activate`.
    * **Atenção:** Caso ocorra um erro de *UnauthorizedAccess* (bloqueio de segurança padrão do PowerShell), execute o seguinte comando para permitir scripts locais: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.
4. Atualize o gerenciador de pacotes: `python.exe -m pip install --upgrade pip`.
5. Instale as dependências do projeto listadas nas instruções: `python -m pip install pandas jupyter seaborn scikit-learn matplotlib plotly statsmodels streamlit joblib`. (Alternativamente, você pode usar `pip install -r requirements.txt`).
6. Para iniciar a interface web, execute o comando: `streamlit run app_vida_util.py`. O sistema abrirá automaticamente no seu navegador.

## Detalhes da Modelagem Preditiva
O desenvolvimento do algoritmo preditivo (`modelagem_hob.ipynb`) seguiu rigorosas etapas de Engenharia de Dados:
* **Limpeza e Seleção:** Foram descartados valores nulos e colunas redundantes que apresentavam multicolinearidade de 100% no *heatmap* de Spearman (como 'Vc m/min', 'CT (S)' e 'Sub-Shift mm').
* **Algoritmo:** Utilizou-se o algoritmo **Random Forest Regressor** para lidar com as relações não-lineares da usinagem.
* **Otimização (Tuning):** O modelo passou por um refinamento via `GridSearchCV` (com Validação Cruzada de 5 partes), testando múltiplas combinações de hiperparâmetros (como `max_depth` e `n_estimators`) para atingir a melhor performance.
* **Performance:** O modelo final alcançou um **R² Score de 0.83** e um Erro Médio Absoluto (MAE) de aproximadamente **109.92 peças**. Este erro foi embarcado no aplicativo para servir como desconto dinâmico e compor a margem estatística de segurança da troca preventiva.

---
<div align="center">
    <i>Desenvolvido por Gabriel Santana</i><br>
    <a href="https://www.linkedin.com/in/santana-gabrielmenezes/" target="_blank">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
    </a>
</div>
