from pathlib import Path
import pandas as pd


def cargar_dataset_procesado(ruta: Path) -> pd.DataFrame:
    """
    Carga el dataset procesado de Fase 2 y convierte la columna date a formato datetime.
    """
    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

    df = pd.read_csv(ruta, parse_dates=["date"])
    return df


def validar_dataset_f3(df: pd.DataFrame) -> None:
    """
    Valida condiciones mínimas del dataset procesado para continuar con la Fase 3.
    """
    columnas_esperadas = (
        ["date", "device", "failure"] +
        [f"metric{i}" for i in range(1, 10)] +
        ["year", "month", "day"]
    )

    columnas_faltantes = [col for col in columnas_esperadas if col not in df.columns]

    assert len(columnas_faltantes) == 0, f"Faltan columnas esperadas: {columnas_faltantes}"
    assert df.shape[0] == 124493, f"Cantidad de filas inesperada: {df.shape[0]}"
    assert df.isnull().sum().sum() == 0, "Existen valores nulos en el dataset."
    assert df.duplicated().sum() == 0, "Existen registros duplicados en el dataset."
    assert pd.api.types.is_datetime64_any_dtype(df["date"]), "La columna date no está en formato datetime."
    assert set(df["failure"].unique()).issubset({0, 1}), "La variable failure contiene valores distintos de 0 y 1."