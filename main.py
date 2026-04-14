from app.infrastructure.loaders import load_file
from app.infrastructure.exporters import export_csv, export_parquet

from app.utils.dataframe_utils import clean_columns, normalize_nulls, normalize_text

from app.application.etl_pipeline import run_cleaning


# 🔥 NUEVO
from app.domain.validators import detectar_filas_corruptas
from app.infrastructure.corrupt_exporter import export_corruptas


from app.config.settings import INPUT_FILE, OUTPUT_PARQUET, OUTPUT_CSV


def main():

    print("Leyendo archivo...")
    df = load_file(INPUT_FILE)

    print("\n--- VALIDACIÓN DE LECTURA ---")
    print(df.iloc[0]["INSTITUCION"])

    # 🔥 LIMPIEZA BASE
    print("Limpiando columnas...")
    df = clean_columns(df)

    print("Normalizando nulls...")
    df = normalize_nulls(df)

    # 🔥 NUEVO: detectar corruptas
    print("Detectando filas corruptas...")
    df, df_corruptas = detectar_filas_corruptas(df)

    export_corruptas(df_corruptas)

    # 🔥 ETL SOLO CON DATOS LIMPIOS
    print("Aplicando reglas de limpieza...")
    df, stats = run_cleaning(df)

    print("\nValores completados:")
    for k, v in stats.items():
        print(k, v)

    print("Normalizando textos...")
    df = normalize_text(df)

    print("\nGuardando resultados...")

    export_parquet(df, OUTPUT_PARQUET)
    export_csv(df, OUTPUT_CSV)

    print("ETL finalizado")


if __name__ == "__main__":
    main()