import ollama

from services.ai.config import OLLAMA_MODEL
from services.ai.prompts.report_prompt import ReportPrompt
from services.ai.providers.base_provider import BaseProvider


class OllamaProvider(BaseProvider):

    def generate_insights(
        self,
        dataset_type,
        profile,
        quality,
        kpis,
    ):

        prompt = ReportPrompt.build(
            dataset_type,
            profile,
            quality,
            kpis,
        )

        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]