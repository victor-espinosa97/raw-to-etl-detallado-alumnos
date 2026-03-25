# untils/dataframe_utils.py

import numpy as np


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