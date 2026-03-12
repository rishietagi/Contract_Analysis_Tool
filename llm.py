import ollama

MODEL = "mistral:latest"

def call_llm(prompt):

    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ],
        options={
            "temperature": 0
        }
    )

    return response["message"]["content"]