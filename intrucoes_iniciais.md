# Observações sobre o sistema

Este código está sendo desenvolvido com o senguinte sistema:
* Windows 11 versão 25H2
* Python versão 3.13.7
* VS Code (VSC) versão 1.131.0
* Terminal Powershell interno ao proprio VSC
* pip versão 26.2.1

# Primeira configuraçao o Ambiente Virtual Python

Estas são as configurações executadas antes do início da criação do código.

1. Abra o VS Code (VSC) no diretório desejado
2. Abra o terminal do Powershel no VSC
3. Execute `python -m venv .venv` para criar um ambiente virtual
4. Execute `.venv\Scripts\activate` para ativar o abiente virtual
    * Caso sucesso: o texto `(.venv)` aparecerá no início da linha de comando do terminal
    * Caso falha:
        * Mensagem de falha:
            ```
            .\venv\Scripts\activate : O arquivo C:\Users\gabri\Desktop\r
            epository\HOB_Tool_Life\venv\Scripts\Activate.ps1 não pode 
            ser carregado porque a execução de scripts foi desabilitada 
            neste sistema. Para obter mais informações, consulte 
            about_Execution_Policies em 
            https://go.microsoft.com/fwlink/?LinkID=135170.
            No linha:1 caractere:1
            + .\venv\Scripts\activate
            + ~~~~~~~~~~~~~~~~~~~~~~~
                + CategoryInfo          : ErrodeSegurança: (:) [], PSSe 
            curityException
                + FullyQualifiedErrorId : UnauthorizedAccess
            ```

            Esse é um bloqueio padrão do sistema operacional. O Windows PowerShell possui uma trava de segurança ativada por padrão (chamada `Restricted`) que impede a execução de scripts automáticos para proteger sua máquina contra códigos maliciosos. Como a ativação do ambiente virtual depende da execução do script `Activate.ps1`, o PowerShell bloqueia o carregamento e gera esse erro de UnauthorizedAccess. Para corrigir isso de forma segura e liberar o seu fluxo de trabalho no VS Code, precisamos alterar a política de execução do PowerShell apenas para o seu usuário logado, permitindo que scripts locais (criados na sua própria máquina) sejam executados.

            ```
            Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
            ```
5. Execute `python -m pip install pandas jupyter seaborn scikit-learn matplotlib plotly statsmodels streamlit joblib` para instalar as principais bibliotecas necessárias para o projeto
6. Execute `python.exe -m pip install --upgrade pip` para atualizar o `pip` para a versão mais recente
7. Execute `pip freeze > requirements.txt` para criar um arquivo `requirements.txt` com todas as bibliotecas instaladas no passo 5
8. Crie um arquivo nomeado `.gitignore`
9. Insira no arquivo `.gitignore` o texto abaixo para que o ambiente virtual seja ignirado durante durante o versionamento com git
    ```
    # Ambientes Virtuais Python
    .venv/
    venv/
    env/
    ENV/
    ```

    **Obs.: É recomendado incluir outras nomenclaturas comuns de ambientes virtuais para garantir que o repositório permaneça limpo mesmo que ambiente virtual seja criado com um nome ligeiramente diferente.**