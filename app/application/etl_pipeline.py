# application/etl_pipeline.py

from app.config.settings import (
    KEY_ESTUDIANTE,
    KEY_INSTITUCION,
    COLUMNAS_POR_ESTUDIANTE,
    COLUMNAS_POR_INSTITUCION,
    COLUMNAS_POR_SEDE
)

from app.domain.rules import completar_por_grupo

def run_cleaning(df):

    stats = {}

    # por estudiante
    for col in COLUMNAS_POR_ESTUDIANTE:
        if col in df.columns:
            df, filled = completar_por_grupo(df, KEY_ESTUDIANTE, col)
            stats[col] = filled

    # por institución
    for col in COLUMNAS_POR_INSTITUCION:
        if col in df.columns:
            df, filled = completar_por_grupo(df, KEY_INSTITUCION, col)
            stats[col] = filled

    # por sede (si tienes clave)
    if "SEDE" in df.columns:
        for col in COLUMNAS_POR_SEDE:
            if col in df.columns:
                df, filled = completar_por_grupo(df, "SEDE", col)
                stats[col] = filled

    return df, stats