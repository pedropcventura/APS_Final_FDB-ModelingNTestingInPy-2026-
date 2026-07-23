from datetime import date

from xbbg import blp


TICKER = "BZPIIPCA Index"
FIELD = "PX_LAST"

START_DATE = "2017-04-01"
END_DATE = date.today().strftime("%Y-%m-%d")

OUTPUT_FILE = "ipca_bloomberg.csv"


def main():
    print(
        f"Baixando {TICKER} de {START_DATE} até {END_DATE}..."
    )

    dados = blp.bdh(
        tickers=TICKER,
        flds=FIELD,
        start_date=START_DATE,
        end_date=END_DATE,

        # Garante que o resultado seja um DataFrame do pandas.
        backend="pandas",

        # Retorna colunas simples: ticker, date e PX_LAST.
        format="semi_long",
    )

    if dados is None or dados.empty:
        raise RuntimeError(
            "A Bloomberg não retornou dados."
        )

    print("\nTipo do objeto retornado:")
    print(type(dados))

    print("\nColunas retornadas:")
    print(dados.columns.tolist())

    print("\nPrimeiras observações:")
    print(dados.head())

    print("\nÚltimas observações:")
    print(dados.tail())

    dados = dados.rename(
        columns={
            "date": "data_bloomberg",
            "PX_LAST": "ipca_index",
        }
    )

    dados = dados[
        [
            "data_bloomberg",
            "ipca_index",
        ]
    ]

    dados.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8-sig",
    )

    print(f"\nArquivo salvo como: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()