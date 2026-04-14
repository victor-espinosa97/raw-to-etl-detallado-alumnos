import pandas as pd


def detectar_filas_corruptas(df):

    def fila_corrupta(row):

        errores = []

        # 🔥 Validación REAL: estructura, no contenido

        # 1. DOC no puede estar vacío
        doc = str(row.get("DOC", "")).strip()
        if doc == "" or doc.lower() == "nan":
            errores.append("DOC vacío")

        # 2. INSTITUCION no puede parecer un número
        institucion = str(row.get("INSTITUCION", "")).strip()
        if institucion.isdigit():
            errores.append("INSTITUCION numérica (columna corrida)")

        # 3. NOMBRE1 no puede ser extremadamente largo
        nombre = str(row.get("NOMBRE1", "")).strip()
        if len(nombre) > 100:
            errores.append("NOMBRE demasiado largo")

        # 4. JORNADA debe ser corta
        jornada = str(row.get("JORNADA", "")).strip()
        if len(jornada) > 20:
            errores.append("JORNADA sospechosa")

        # 5. DETECCIÓN CLAVE (la más importante)
        # si ESTADO aparece donde no debe
        if doc.upper() in ["MATRICULADO", "RETIRADO"]:
            errores.append("columnas corridas (DOC contiene ESTADO)")

        # 🔥 marcar error
        if errores:
            row["__errores__"] = ", ".join(errores)
            return True

        return False

    mask_corruptas = df.apply(fila_corrupta, axis=1)

    df_corruptas = df[mask_corruptas]
    df_validas = df[~mask_corruptas]

    return df_validas, df_corruptas