import numpy as np # type: ignore

def calcular_metricas(y_real, y_pred):
    y_real = np.asarray(y_real)
    y_pred = np.asarray(y_pred)
    mae = np.mean(np.abs(y_real - y_pred))
    rmse = np.sqrt(np.mean((y_real - y_pred) ** 2))
    return {"MAE": round(mae, 4), "RMSE": round(rmse, 4)}
