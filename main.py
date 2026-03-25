from app.infrastructure.loaders import load_file
from app.infrastructure.exporters import export_csv, export_parquet

from app.utils.dataframe_utils import clean_columns, normalize_nulls

from app.application.etl_pipeline import run_cleaning

from app.config.settings import INPUT_FILE, OUTPUT_PARQUET, OUTPUT_CSV


def main():

    print("Leyendo archivo...")
    df = load_file(INPUT_FILE)

    print("Limpiando columnas...")
    df = clean_columns(df)

    print("Normalizando nulls...")
    df = normalize_nulls(df)

    print("Aplicando reglas de limpieza...")
    df, stats = run_cleaning(df)

    print("\nValores completados:")
    for k, v in stats.items():
        print(k, v)

    print("\nGuardando resultados...")

    export_parquet(df, OUTPUT_PARQUET)
    export_csv(df, OUTPUT_CSV)

    print("ETL finalizado")


if __name__ == "__main__":
    main()