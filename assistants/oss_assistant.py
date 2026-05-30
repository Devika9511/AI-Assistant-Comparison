import requests

def generate_response(messages):

    prompt = messages[-1]["content"]

    try:

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen2.5:0.5b",
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        return response.json()["response"]

    except Exception as e:

        return f"OSS Error: {str(e)}"