import numpy as np  # type: ignore

try:
    import pandas as pd
    import pandas as pandas_module
except ImportError:  # pragma: no cover - el entorno de ejecución puede no tener pandas instalado
    class _PandasFallback:
        Series = object
        DataFrame = object

    pd = None  # type: ignore[assignment]
    pandas_module = _PandasFallback()


class ModeloSeriesTemporales:
    """Modelo de referencia con implementación útil para series temporales.

    Proporciona dos estrategias simples: media móvil y persistencia.
    """

    def __init__(self, window: int = 24):
        self.window = max(int(window), 1)
        self._ultimo_valor: float | None = None

    def entrenar(self, train: "pandas_module.Series", window: int | None = None) -> float:
        """Entrena el modelo sobre la serie y devuelve el valor estimado actual."""
        if window is not None:
            self.window = max(int(window), 1)

        if train.empty:
            raise ValueError("La serie de entrenamiento no puede estar vacía.")

        valor = train.rolling(window=self.window).mean().iloc[-1]
        self._ultimo_valor = float(valor)
        return self._ultimo_valor

    def predecir(self, train: "pandas_module.Series", pasos: int = 1) -> np.ndarray:
        """Predice los próximos pasos usando persistencia sobre el último valor entrenado."""
        if self._ultimo_valor is None:
            self.entrenar(train)

        pasos = max(int(pasos), 1)
        return np.full(pasos, self._ultimo_valor, dtype=float)


def entrenar_prediccion_media_movil(train: "pandas_module.Series", window=24) -> float:
    """Baseline: Promedio móvil simple de las últimas 24 horas."""
    if train.empty:
        raise ValueError("La serie de entrenamiento no puede estar vacía.")
    return float(train.rolling(window=window).mean().iloc[-1])


def predecir_persistencia(train: "pandas_module.Series", pasos: int) -> np.ndarray:
    """Baseline Persistencia: El valor futuro equivale al último valor observado."""
    ultimo_valor = train.iloc[-1]
    return np.full(max(int(pasos), 1), ultimo_valor, dtype=float)