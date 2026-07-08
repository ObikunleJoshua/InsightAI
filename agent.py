import ollama

def ask_agent(question, dataset_summary):

    prompt = f"""
You are a senior business data analyst.

Dataset Summary:

{dataset_summary}

User Question:
{question}

Instructions:

- Use the dataset statistics provided.
- Give direct answers.
- Mention key numbers.
- Provide business recommendations.
- Be concise.
"""

    response = ollama.chat(
        model="qwen3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]