import ollama

response = ollama.chat(
    model="qwen3",
    messages=[
        {
            "role": "user",
            "content": "Say hello."
        }
    ]
)

print(response["message"]["content"])