import pandas as pd  # type: ignore

def preparar_serie_temporal(df: pd.DataFrame) -> pd.DataFrame:
    """Valida, ordena y limpia la serie temporal."""
    df = df.copy()
    df = df.dropna()
    df = df.sort_values('fecha_hora').reset_index(drop=True)
    df.set_index('fecha_hora', inplace=True)
    return df