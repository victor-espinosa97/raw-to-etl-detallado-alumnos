# infrastructure/exporters.py

import csv

def export_parquet(df, path):
    df.to_parquet(path, index=False)


def export_csv(df, path):
    df.to_csv(
        path,
        sep=";",
        index=False,
        encoding="utf-8-sig",
        quoting=csv.QUOTE_ALL,
        escapechar="\\",
        lineterminator="\n"
    )