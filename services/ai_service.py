import ollama

class AIService:
    """Generates AI-powered insights from computed analytics."""

    MODEL = "qwen3:4b"

    @staticmethod
    def generate_insights(dataset_type, profile, quality, kpis):

        prompt = f"""
You are a Senior Business Intelligence Analyst.

Analyze the following dataset summary.

Dataset Type:
{dataset_type["label"]}

Quality Score:
{quality["score"]}%

Rows:
{profile["rows"]}

Columns:
{profile["columns"]}

Missing Values:
{profile["missing_values"]}

KPIs:
{kpis}

Write:

1. Executive Summary

2. Three Key Findings

3. Three Recommendations

Keep the response under 300 words.

Keep the report professional.

Do NOT invent numbers.

Use only the information provided.
"""

        prompt = prompt[:3000]

        response = ollama.chat(
            model=AIService.MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]