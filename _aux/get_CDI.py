from datetime import date

from xbbg import blp


TICKER = "IDIX9 Index"
FIELD = "PX_LAST"

START_DATE = "2017-04-01"
END_DATE = date.today().strftime("%Y-%m-%d")

OUTPUT_FILE = "cdi_bloomberg.csv"


def main():
    print(
        f"Baixando {TICKER} de {START_DATE} até {END_DATE}..."
    )

    dados = blp.bdh(
        tickers=TICKER,
        flds=FIELD,
        start_date=START_DATE,
        end_date=END_DATE,

        # Evita o problema do DataFrame Polars.
        backend="pandas",
        format="semi_long",
    )

    if dados is None or dados.empty:
        raise RuntimeError(
            "A Bloomberg não retornou dados para o CDI."
        )

    print("\nColunas retornadas:")
    print(dados.columns.tolist())

    dados = dados.rename(
        columns={
            "date": "data",
            "PX_LAST": "cdi_index",
        }
    )

    dados = dados[
        [
            "data",
            "cdi_index",
        ]
    ].copy()

    # Retorno diário do CDI.
    dados["cdi_retorno_diario_pct"] = (
        dados["cdi_index"]
        .pct_change()
        .mul(100)
    )

    # Retorno acumulado desde 1º de abril de 2017.
    dados["cdi_acumulado_desde_inicio_pct"] = (
        dados["cdi_index"]
        .div(dados["cdi_index"].iloc[0])
        .sub(1)
        .mul(100)
    )

    print("\nPrimeiras observações:")
    print(dados.head())

    print("\nÚltimas observações:")
    print(dados.tail())

    dados.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8-sig",
    )

    print(f"\nArquivo salvo como: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()