
import requests

MODEL = "qwen2.5:3b"
OLLAMA_URL = "http://localhost:11434/api/chat"


def ask_ollama(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "stream": False
            },
            timeout=180
        )
        response.raise_for_status()
        return response.json()["message"]["content"]

    except requests.exceptions.RequestException as error:
        print("Ollama connection error:", error)
        return "Unable to connect to Ollama. Check that Ollama is running."
