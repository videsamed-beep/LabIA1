import requests

def probar_ollama():
    url = "http://localhost:11434/api/generate"
    
    payload = {
        "model": "qwen2.5-coder:7b",  # Cambia por el nombre del modelo que tengas descargado en Ollama
        "prompt": "¿Qué es la cuantización en IA?",
        "stream": False
    }

    try:
        # Es muy importante usar requests.post y NO requests.get
        response = requests.post(url, json=payload)
        response.raise_for_status()
        
        datos = response.json()
        print("\n--- Respuesta de Ollama ---")
        print(datos.get("response"))
        
    except requests.exceptions.HTTPError as err:
        print(f"Error HTTP: {err}")
    except Exception as e:
        print(f"Error de conexión: {e}")

if __name__ == "__main__":
    probar_ollama()
