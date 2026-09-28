import matplotlib.pyplot as plt # type: ignore
from api_client import obtener_datos_meteorologicos
from preprocessing import preparar_serie_temporal
from model import predecir_persistencia
from evaluation import calcular_metricas

def ejecutar_pipeline():
    # 1. Obtención y preparación
    raw_df = obtener_datos_meteorologicos()
    df = preparar_serie_temporal(raw_df)
    
    # 2. División Train / Test sin violar temporalidad
    split_idx = int(len(df) * 0.8)
    train, test = df.iloc[:split_idx], df.iloc[split_idx:]
    
    # 3. Predicción (Persistencia baseline)
    predicciones = predecir_persistencia(train['temperatura'], pasos=len(test))
    test = test.assign(prediccion=predicciones)
    
    # 4. Evaluación
    metricas = calcular_metricas(test['temperatura'], test['prediccion'])
    print("Métricas de Evaluación:", metricas)
    
    # 5. Visualización
    plt.figure(figsize=(12, 6))
    plt.plot(train.index, train['temperatura'], label='Entrenamiento (Real)')
    plt.plot(test.index, test['temperatura'], label='Prueba (Real)', color='green')
    plt.plot(test.index, test['prediccion'], label='Predicción (Baseline)', linestyle='--', color='red')
    plt.title('Serie Temporal de Temperatura y Predicción Baseline')
    plt.xlabel('Fecha/Hora')
    plt.ylabel('Temperatura (°C)')
    plt.legend()
    plt.grid(True)
    plt.savefig('evidence/serie_temporal_grafica.png')
    plt.show()

if __name__ == "__main__":
    ejecutar_pipeline()