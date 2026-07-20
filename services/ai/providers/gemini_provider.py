from google import genai

from services.ai.config import GEMINI_API_KEY, GEMINI_MODEL
from services.ai.prompts.report_prompt import ReportPrompt
from services.ai.providers.base_provider import BaseProvider


class GeminiProvider(BaseProvider):

    def generate_insights(
        self,
        dataset_type: dict,
        metadata: dict,
        quality: dict,
        kpis: dict,
    ) -> str:

        prompt = ReportPrompt.build(
            dataset_type,
            metadata,
            quality,
            kpis,
        )

        client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
        )

        return response.text