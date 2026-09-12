# app.py
import pandas as pd
import streamlit as st
from scraper import buscar_livros, buscar_bolsas

# Inicializa as chaves de session_state ANTES de qualquer uso
if "meus_livros" not in st.session_state:
    st.session_state.meus_livros = None

if "pagina_grafico" not in st.session_state:
    st.session_state.pagina_grafico = 0

if "bolsas" not in st.session_state:
    st.session_state.bolsas = None

st.markdown(
    """
    <style>
    @keyframes rainbow {
        0% { color: red; }
        16% { color: orange; }
        33% { color: yellow; }
        50% { color: green; }
        66% { color: blue; }
        83% { color: indigo; }
        100% { color: violet; }
    }
    .rainbow-text {
        font-size: 3rem;
        font-weight: bold;
        animation: rainbow 4s infinite linear;
    }
    </style>
    <h1 class="rainbow-text">Buscador de Livros</h1>
    """,
    unsafe_allow_html=True,
)

st.write(
    ":yellow[***Procurando algum livro no books to scrape?***]\n\n"
    "*Busque por eles e veja o que há de melhor*!"
)

# Ao clicar, salva o DataFrame retornado dentro da chave 'meus_livros'
if st.button("**Buscar Livros Irados**"):
    with st.spinner("Buscando..."):
        st.session_state.meus_livros = buscar_livros()
        st.session_state.pagina_grafico = (
            0  # reinicia a página do gráfico a cada nova busca
        )

# Verifica a chave correta da memória 'meus_livros'
if st.session_state.meus_livros is not None:
    df_resultado = st.session_state.meus_livros

    if df_resultado.empty:
        st.warning("Nenhum livro encontrado.")
    else:
        st.markdown("### 📋 Lista de Livros Disponíveis")
        st.dataframe(df_resultado, use_container_width=True)

        st.markdown("### 📊 Comparação de Preços")

        livros_por_pagina = 20
        total_paginas = -(-len(df_resultado) // livros_por_pagina)  # arredonda pra cima

        inicio = st.session_state.pagina_grafico * livros_por_pagina
        fim = inicio + livros_por_pagina
        df_pagina = df_resultado.iloc[inicio:fim]

        st.bar_chart(data=df_pagina, x="Título", y="Preço", color="#0C5CF0")

        coluna_esquerda, coluna_meio, coluna_direita = st.columns([1, 2, 1])

        with coluna_esquerda:
            if st.button("◀ Anterior", disabled=(st.session_state.pagina_grafico == 0)):
                st.session_state.pagina_grafico -= 1
                st.rerun()

        with coluna_meio:
            st.write(f"Página {st.session_state.pagina_grafico + 1} de {total_paginas}")

        with coluna_direita:
            if st.button(
                "Próxima ▶",
                disabled=(st.session_state.pagina_grafico >= total_paginas - 1),
            ):
                st.session_state.pagina_grafico += 1
                st.rerun()


st.divider()


st.markdown(
    """
    <style>
    @keyframes rainbow {
        0% { color: red; }
        16% { color: orange; }
        33% { color: yellow; }
        50% { color: green; }
        66% { color: blue; }
        83% { color: indigo; }
        100% { color: violet; }
    }
    .rainbow-text {
        font-size: 3rem;
        font-weight: bold;
        animation: rainbow 4s infinite linear;
    }
    </style>
    <h1 class="rainbow-text">Buscador de bolsas</h1>
    """,
    unsafe_allow_html=True,
)

st.write(
    ":yellow[***Aqui você pode pesquisar por uma bolsa usando uma API!***]\n\n"
    "*Boa pesquisa*!"
)


def verificacao():
    if isinstance(st.session_state.bolsas, tuple):
        tabela = st.session_state.bolsas[0]
        media = st.session_state.bolsas[1]
        eod = st.session_state.bolsas[2]

        st.bar_chart(data=tabela, x="date", y="close", color="#0C5CF0")

        m, e = st.columns([1, 1])
        m.metric(label="Média do fechamento mensal", value=round(media, 2))
        e.metric(label="valor de fechamento diario", value=round(eod, 2))
    else:
        st.warning("A bolsa não foi encontrada")


def comparacao(resultado_bolsas):
    if isinstance(resultado_bolsas, tuple):
        media = resultado_bolsas[1]
        eod = resultado_bolsas[2]
        return round(media, 2), round(eod, 2)
    else:
        st.warning("A bolsa não existe....")
        return None, None


pesquisa_bolsas = st.text_input("Qual bolsa gostaria de pesquisar?")

if st.button("Buscar bolsa"):
    with st.spinner("Buscando bolsas..."):
        st.session_state.bolsas = buscar_bolsas(pesquisa=pesquisa_bolsas)


if st.session_state.bolsas is not None:
    verificacao()


st.divider()

# Versus

st.markdown(
    """
    <style>
    @keyframes rainbow {
        0% { color: red; }
        16% { color: orange; }
        33% { color: yellow; }
        50% { color: green; }
        66% { color: blue; }
        83% { color: indigo; }
        100% { color: violet; }
    }
    .rainbow-text {
        font-size: 3rem;
        font-weight: bold;
        animation: rainbow 4s infinite linear;
    }
    </style>
    <h1 class="rainbow-text">Comparador de bolsas</h1>
    """,
    unsafe_allow_html=True,
)

Versus1 = st.text_input("Primeira bolsa")
Versus2 = st.text_input("Segunda bolsa")

if st.button("Comparar"):
    with st.spinner("Buscando bolsas..."):
        bolsa1 = buscar_bolsas(pesquisa=Versus1)
        bolsa2 = buscar_bolsas(pesquisa=Versus2)
        media1, eod1 = comparacao(resultado_bolsas=bolsa1)
        media2, eod2 = comparacao(resultado_bolsas=bolsa2)

        dicionario_comp = {
            "Bolsa": [Versus1, Versus2],
            "Média": [media1, media2],
            "Fechamento": [eod1, eod2],
        }

        dataframe = pd.DataFrame(dicionario_comp)

        st.bar_chart(data=dataframe, x="Bolsa", y="Média")
        st.bar_chart(data=dataframe, x="Bolsa", y="Fechamento")
