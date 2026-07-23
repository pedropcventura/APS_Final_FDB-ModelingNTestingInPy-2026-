# Futuros Agropecuários como Hedge contra a Inflação no Brasil

Projeto final da eletiva **Financial Databases: Modeling and Testing in Python**.

> **Não é necessário executar o projeto.**  
> O arquivo `main.ipynb` já está salvo com os resultados, tabelas e gráficos gerados, acompanhados das explicações. Basta abri-lo no VS Code para visualizar o trabalho completo.
>
> As instruções abaixo são apenas para quem desejar executar novamente todas as células.

## Estrutura do projeto

```text
.
├── main.ipynb
└── _aux
    ├── data
    │   ├── cdi_bloomberg.csv
    │   ├── datas_divulgacao_ipca_ibge.csv
    │   ├── IFBOI.xlsx
    │   ├── IFMILHO.xlsx
    │   └── ipca_bloomberg.csv
    ├── get_CDI.py
    ├── get_IPCA.py
    ├── IPCA_dates.py
    └── ssrn-1730243.pdf
```

### Arquivos principais

- `main.ipynb`: notebook principal, com tratamento dos dados, gráficos, testes estatísticos e resultados.
- `_aux/data/ipca_bloomberg.csv`: série histórica do IPCA obtida na Bloomberg.
- `_aux/data/cdi_bloomberg.csv`: série histórica do CDI obtida na Bloomberg.
- `_aux/data/datas_divulgacao_ipca_ibge.csv`: datas oficiais de divulgação do IPCA, coletadas no IBGE.
- `_aux/data/IFBOI.xlsx`: série e metodologia do índice futuro de boi gordo da B3.
- `_aux/data/IFMILHO.xlsx`: série e metodologia do índice futuro de milho da B3.
- `_aux/get_IPCA.py`: script usado para baixar o IPCA da Bloomberg.
- `_aux/get_CDI.py`: script usado para baixar o CDI da Bloomberg.
- `_aux/IPCA_dates.py`: script usado para coletar as datas de divulgação do IPCA no IBGE.
- `_aux/ssrn-1730243.pdf`: artigo de Spierdijk e Umar que inspirou o projeto.

> Os arquivos CSV e XLSX necessários já estão incluídos. Portanto, para executar apenas o `main.ipynb`, não é necessário ter acesso à Bloomberg.

## Como executar no VS Code

### 1. Requisitos

Instale:

- [Python](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/)
- No VS Code, as extensões **Python** e **Jupyter**, publicadas pela Microsoft.

Abra no VS Code a pasta raiz do projeto, ou seja, a pasta que contém `main.ipynb` e `_aux`.

### 2. Criar o ambiente virtual

No VS Code, abra **Terminal > New Terminal** e execute:

```powershell
py -m venv venv
```

Ative o ambiente:

```powershell
.\venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativação, execute primeiro:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Em seguida, tente novamente:

```powershell
.\venv\Scripts\Activate.ps1
```

Quando o ambiente estiver ativo, o terminal mostrará `(venv)` no início da linha.

### 3. Instalar as dependências

Com o ambiente virtual ativo, execute:

```powershell
py -m pip install --upgrade pip
py -m pip install pandas numpy matplotlib statsmodels openpyxl jupyter ipykernel
```

### 4. Selecionar o kernel do notebook

Abra o arquivo `main.ipynb`.

No canto superior direito do notebook, clique em **Select Kernel** e escolha o Python localizado em:

```text
venv\Scripts\python.exe
```

Normalmente ele aparece como:

```text
Python (venv)
```

### Se o ambiente não aparecer na lista de kernels

Com o `venv` ativo no terminal, execute:

```powershell
py -m ipykernel install --user --name aps-final --display-name "Python (APS Final)"
```

Depois:

1. Feche e abra novamente o VS Code.
2. Abra `main.ipynb`.
3. Clique em **Select Kernel**.
4. Escolha **Python (APS Final)**.

Se ainda não aparecer:

1. Pressione `Ctrl + Shift + P`.
2. Pesquise por **Python: Select Interpreter**.
3. Selecione **Enter interpreter path**.
4. Escolha manualmente:

```text
<PASTA_DO_PROJETO>\venv\Scripts\python.exe
```

Depois volte ao notebook e selecione esse mesmo ambiente como kernel.

### 5. Executar o notebook

No arquivo `main.ipynb`, clique em:

```text
Run All
```

ou execute as células individualmente, de cima para baixo.

> É importante abrir a pasta raiz completa do projeto no VS Code. Caso apenas o arquivo `main.ipynb` seja aberto isoladamente, os caminhos relativos para a pasta `_aux/data` podem não funcionar.

## Scripts que usam Bloomberg

Os scripts abaixo só podem ser executados em um computador que tenha:

- Bloomberg Terminal instalado;
- usuário conectado no Terminal;
- acesso autorizado à Bloomberg Desktop API;
- pacote `xbbg` instalado.

```text
_aux/get_IPCA.py
_aux/get_CDI.py
```

Para instalar a dependência adicional desses scripts:

```powershell
py -m pip install xbbg
```

O script `_aux/IPCA_dates.py` não depende da Bloomberg. Ele consulta dados públicos do IBGE e pode exigir:

```powershell
py -m pip install requests beautifulsoup4
```

Esses scripts auxiliares não precisam ser executados para reproduzir o notebook, pois os arquivos de dados já estão salvos em `_aux/data`.

## Observação final

O projeto foi desenvolvido e testado no **Visual Studio Code**, em ambiente Windows, utilizando um ambiente virtual Python.
