import re
from datetime import date

import pandas as pd
import requests
from bs4 import BeautifulSoup


URL_IBGE = (
    "https://www.ibge.gov.br/estatisticas/economicas/"
    "precos-e-custos/9256-indice-nacional-de-precos-"
    "ao-consumidor-amplo.html"
)

OUTPUT_FILE = "datas_divulgacao_ipca_ibge.csv"


def main():
    print("Baixando o calendário do IPCA no IBGE...")

    response = requests.get(
        URL_IBGE,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=30,
    )

    # Interrompe o programa se a página não for carregada.
    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser",
    )

    # Converte todo o HTML em um único texto.
    texto = " ".join(soup.stripped_strings)

    # Remove espaços repetidos.
    texto = re.sub(
        r"\s+",
        " ",
        texto,
    )

    # Procura estruturas como:
    #
    # Período de referência: 6/2026 10/07/2026
    #
    # Algumas observações antigas aparecem assim:
    #
    # Período de referência:
    # 4/2018 a 4/2018 10/05/2018

    padrao = re.compile(
        r"Período de referência:\s*"
        r"(\d{1,2})/(\d{4})"
        r"(?:\s+a\s+\d{1,2}/\d{4})?\s+"
        r"(\d{2}/\d{2}/\d{4})"
    )

    registros = []

    for mes, ano, data_divulgacao in padrao.findall(texto):
        periodo_referencia = pd.Period(
            year=int(ano),
            month=int(mes),
            freq="M",
        )

        data_divulgacao = pd.to_datetime(
            data_divulgacao,
            format="%d/%m/%Y",
        )

        registros.append(
            {
                "periodo_referencia": periodo_referencia,
                "data_divulgacao": data_divulgacao,
            }
        )

    dados = pd.DataFrame(registros)

    if dados.empty:
        raise RuntimeError(
            "Nenhuma data de divulgação foi encontrada "
            "na página do IBGE."
        )

    primeiro_periodo = pd.Period(
        "2017-04",
        freq="M",
    )

    hoje = pd.Timestamp(date.today())

    # Mantém somente:
    # 1. meses desde abril de 2017;
    # 2. divulgações que já aconteceram.
    dados = dados[
        (dados["periodo_referencia"] >= primeiro_periodo)
        & (dados["data_divulgacao"] <= hoje)
    ].copy()

    # Evita duplicidades.
    dados = dados.drop_duplicates(
        subset="periodo_referencia",
        keep="first",
    )

    # Ordena do mês mais antigo ao mais recente.
    dados = dados.sort_values(
        "periodo_referencia",
    ).reset_index(drop=True)

    # Transforma 2017-04, 2017-05 etc. em texto.
    dados["periodo_referencia"] = (
        dados["periodo_referencia"].astype(str)
    )

    print("\nPrimeiras observações:")
    print(dados.head())

    print("\nÚltimas observações:")
    print(dados.tail())

    print(f"\nQuantidade de meses: {len(dados)}")

    dados.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8-sig",
        date_format="%Y-%m-%d",
    )

    print(f"\nArquivo salvo como: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()