# infrastructure/exporters.py

def export_parquet(df, path):

    df.to_parquet(path, index=False)


def export_csv(df, path):

    df.to_csv(path, sep=";", index=False)