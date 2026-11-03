# lógica do scraper vai aqui
import os
from bs4 import BeautifulSoup as bs
import requests as rqs
import pandas as pd
import streamlit as st


@st.cache_data
def buscar_livros():

    link = "https://books.toscrape.com/catalogue/page-{}.html"

    dados_livros = {"Título": [], "Preço": []}

    for pagina in range(1, 6):
        url = link.format(pagina)
        requisição = rqs.get(url)

        site = bs(requisição.text, "html.parser")
        # acesso geral do BLOCO do livro, da pra ir "aprofundando" o find
        livros = site.find_all("article", class_="product_pod")

        # filtragem dos titulos e preços
        for livros in livros:

            titulo = livros.find("h3").find("a")["title"]

            precos = livros.find("p", class_="price_color").get_text()

            texto_filtrado = "".join(
                filter(lambda numero: numero.isdigit() or numero == ".", precos)
            )

            dados_livros["Título"].append(titulo)

            dados_livros["Preço"].append(float(texto_filtrado))

    dataframe = pd.DataFrame(dados_livros)

    return dataframe


# agora usando API


@st.cache_data(ttl=86400)
def buscar_bolsas(pesquisa):

    chave_api = os.environ.get("CHAVE_API")

    url = f"https://api.marketstack.com/v2/eod?access_key={chave_api}&symbols={pesquisa}&limit=30&sort=DESC"

    requisicao = rqs.get(url)

    if requisicao.status_code != 200:

        return "Parece que essa bolsa não existe..."
    else:

        dados = requisicao.json()

        tabela = pd.DataFrame(dados["data"])

        acessar = tabela["close"]

        eod = tabela["close"].iloc[0]

        media = acessar.mean()

        return tabela, media, eod


if __name__ == "__main__":
    resultado = buscar_livros(), buscar_bolsas()
    print(resultado)
