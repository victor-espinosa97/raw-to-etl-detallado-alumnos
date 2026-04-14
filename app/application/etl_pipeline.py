# application/etl_pipeline.py

from app.config.settings import (
    KEY_ESTUDIANTE,
    KEY_INSTITUCION,
    COLUMNAS_POR_ESTUDIANTE,
    COLUMNAS_POR_INSTITUCION,
    COLUMNAS_POR_SEDE,
    COLUMNAS_FECHA
)

from app.domain.rules import completar_por_grupo


def run_cleaning(df):

    stats = {}

    # 🔥 IMPORTANTE: forzar strings en keys de agrupación
    for key in [KEY_ESTUDIANTE, KEY_INSTITUCION, "SEDE"]:
        if key in df.columns:
            df[key] = df[key].astype(str)

    # 1. estudiante
    for col in COLUMNAS_POR_ESTUDIANTE:
        if col in df.columns:
            df, filled = completar_por_grupo(df, KEY_ESTUDIANTE, col)
            stats[col] = filled

    # 2. institución
    for col in COLUMNAS_POR_INSTITUCION:
        if col in df.columns:
            df, filled = completar_por_grupo(df, KEY_INSTITUCION, col)
            stats[col] = filled

    # 3. sede
    if "SEDE" in df.columns:
        for col in COLUMNAS_POR_SEDE:
            if col in df.columns:
                df, filled = completar_por_grupo(df, "SEDE", col)
                stats[col] = filled

    # 4. fechas (último paso)
    for col in COLUMNAS_FECHA:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.split(" ").str[0]
                .str.replace("-", "/", regex=False)
            )

    return df, stats