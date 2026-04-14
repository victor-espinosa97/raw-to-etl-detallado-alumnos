# untils/dataframe_utils.py

import numpy as np

import unicodedata


import unicodedata

def quitar_tildes_pero_enie(texto):

    if not isinstance(texto, str):
        return texto

    resultado = []

    for c in texto:
        # mantener ñ y Ñ intactas
        if c in ("ñ", "Ñ"):
            resultado.append(c)
            continue

        # normalizar solo el carácter
        descompuesto = unicodedata.normalize("NFD", c)

        # quitar tildes (acentos)
        descompuesto = "".join(
            ch for ch in descompuesto
            if unicodedata.category(ch) != "Mn"
        )

        resultado.append(descompuesto)

    return "".join(resultado)

def normalize_text(df):
    import pandas as pd

    text_columns = df.select_dtypes(include=["object"]).columns

    for col in text_columns:
        df[col] = df[col].map(
            lambda x: quitar_tildes_pero_enie(x) if isinstance(x, str) else x
        )

    return df

def clean_columns(df):

    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_")
        .str.upper()
    )

    return df


def normalize_nulls(df):

    null_values = ["", " ", "NULL", "None", "nan"]

    return df.replace(null_values, np.nan)