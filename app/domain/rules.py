# domain/rules.py

import pandas as pd


def completar_por_grupo(df, key, columna):

    before = df[columna].isna().sum()

    df[columna] = (
        df.groupby(key)[columna]
        .transform(lambda x: x.ffill().bfill())
    )

    after = df[columna].isna().sum()

    return df, before - after