# 📚 Webscraping — Buscador e Analisador de Dados

Uma aplicação web desenvolvida em Python que combina técnicas de **Web Scraping, consumo de APIs e visualização de dados** para transformar informações disponíveis na internet em resultados organizados e interativos.

O projeto utiliza o Streamlit para oferecer uma interface simples e intuitiva, permitindo consultar catálogos de livros, acompanhar dados históricos de ações e comparar indicadores financeiros.

## ✨ Funcionalidades

### 📖 1. Buscador de livros

Realiza a extração automatizada de informações do catálogo do [Books to Scrape](https://books.toscrape.com/).

- Consulta as cinco primeiras páginas do catálogo.
- Extrai títulos e preços dos livros.
- Organiza os resultados em uma tabela interativa.
- Apresenta gráficos para comparação de preços.
- Utiliza cache para evitar requisições desnecessárias.

### 📈 2. Buscador de ações

Integração com a API da [Marketstack](https://marketstack.com/) para consultar informações financeiras.

- Pesquisa ativos utilizando seus símbolos de identificação (tickers).
- Obtém dados históricos de fechamento.
- Calcula a média dos preços de fechamento retornados.
- Apresenta o último fechamento disponível na consulta.
- Exibe gráficos com a evolução dos preços.

### ⚖️ 3. Comparador de ações

Permite comparar dois ativos financeiros simultaneamente.

- Consulta dois símbolos de ativos.
- Compara as médias dos preços de fechamento.
- Compara os últimos preços de fechamento disponíveis.
- Apresenta gráficos para facilitar a análise.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3.11 | Linguagem de programação |
| Streamlit | Desenvolvimento da interface web |
| Requests | Comunicação HTTP |
| BeautifulSoup4 | Extração de informações HTML |
| Pandas | Manipulação e organização de dados |
| Marketstack API | Obtenção de dados financeiros |

## 📂 Estrutura do projeto

```text
Webscraping/
│
├── .devcontainer/
│   └── devcontainer.json
│
├── .streamlit/
│   └── secrets.toml          # Configuração local da API
│
├── app.py                    # Interface principal
├── scraper.py                # Lógica de extração de dados
├── utils.py                  # Módulo de funções auxiliares
│
├── requirements.txt          # Dependências do projeto
├── .gitignore
└── .gitattributes
```

### Descrição dos arquivos

**`app.py`**

Arquivo principal da aplicação. Responsável por construir a interface utilizando Streamlit, receber as entradas do usuário, executar as pesquisas e apresentar os resultados.

**`scraper.py`**

Contém as funções responsáveis pela obtenção e processamento dos dados:

- `buscar_livros()`: realiza o scraping do catálogo de livros.
- `buscar_bolsas(pesquisa)`: consulta a API Marketstack e processa os dados financeiros.

**`utils.py`**

Reservado para funções auxiliares e futuras melhorias na organização do código.

**`requirements.txt`**

Contém as bibliotecas necessárias para executar a aplicação.

**`.devcontainer/devcontainer.json`**

Define o ambiente de desenvolvimento, incluindo a versão do Python, extensões do VS Code, instalação das dependências e inicialização automática da aplicação.

## 🚀 Instalação e execução

### 1. Pré-requisitos

- Python 3.11 ou superior.
- Git.
- Uma chave de API da [Marketstack](https://marketstack.com/) para utilizar as funcionalidades financeiras.

### 2. Clonar o repositório

```bash
git clone https://github.com/Pietro-P-T/Webscraping.git

cd Webscraping
```

### 3. Criar um ambiente virtual

```bash
python -m venv venv
```

Ative o ambiente virtual:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Configurar a chave da API

Crie o arquivo `secrets.toml` dentro da pasta `.streamlit`:

```toml
CHAVE_API = "sua_chave_api_aqui"
```

Substitua o valor pela chave obtida na Marketstack.

**Importante:** não compartilhe sua chave de API publicamente nem a envie para o GitHub. Mantenha o arquivo de segredos fora do controle de versão.

### 6. Executar a aplicação

```bash
streamlit run app.py
```

Após a inicialização, o Streamlit disponibilizará a aplicação localmente, normalmente em:

```text
http://localhost:8501
```

## 💻 Exemplos de utilização

### Pesquisa de livros

1. Acesse a seção de busca de livros.
2. Clique em **Buscar Livros Irados**.
3. Aguarde a extração das informações.
4. Consulte a tabela com os títulos e preços.
5. Utilize os controles de paginação para navegar pelos gráficos de comparação.

### Pesquisa de ações

1. Acesse a seção de busca de bolsas.
2. Digite o símbolo de identificação do ativo.
3. Clique em **Buscar bolsa**.
4. Consulte o gráfico histórico e os indicadores apresentados.

### Comparação de ações

1. Acesse a seção Comparador de bolsas.
2. Informe o primeiro ativo.
3. Informe o segundo ativo.
4. Clique em **Comparar**.
5. Analise os gráficos de médias e fechamentos.

## 🧠 Funcionamento técnico

A aplicação utiliza uma arquitetura modular, separando a interface visual da lógica responsável pela obtenção dos dados.

```text
                  USUÁRIO
                     |
                     v
              STREAMLIT (app.py)
                     |
          +----------+----------+
          |                     |
          v                     v
     BUSCAR LIVROS        BUSCAR AÇÕES
          |                     |
          v                     v
      REQUESTS             REQUESTS
          |                     |
          v                     v
   BOOKS TO SCRAPE       MARKETSTACK API
          |                     |
          v                     v
    BEAUTIFULSOUP          RESPOSTA JSON
          |                     |
          +----------+----------+
                     |
                     v
                 PANDAS
                     |
                     v
             VISUALIZAÇÃO
               STREAMLIT
```

O Streamlit também utiliza mecanismos de cache para armazenar resultados de consultas, reduzindo requisições repetidas e melhorando a experiência de utilização.


## 👨‍💻 Autor

**Pietro Pianaro Tiburtino**

GitHub: [@Pietro-P-T](https://github.com/Pietro-P-T)

Repositório: [Webscraping](https://github.com/Pietro-P-T/Webscraping)
