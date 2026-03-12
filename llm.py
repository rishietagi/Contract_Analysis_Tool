import ollama

MODEL = "mistral:latest"

def call_llm(prompt):

    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ],
        options={
            "temperature": 0,
            "top_p": 0.9

        }
    )

    return response["message"]["content"]