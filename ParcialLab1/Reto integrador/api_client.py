import requests
import pandas as pd  # type: ignore

def obtener_datos_meteorologicos(latitud=6.053, longitud=-75.402, dias=30):
    """Obtiene datos de temperatura horaria de los últimos días desde la API de Open-Meteo."""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&past_days={dias}&hourly=temperature_2m"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    df = pd.DataFrame({
        'fecha_hora': pd.to_datetime(data['hourly']['time']),
        'temperatura': data['hourly']['temperature_2m']
    })
    return df
