import time

from google import genai
from google.genai.errors import ClientError, ServerError

from services.ai.config import GEMINI_API_KEY, GEMINI_MODEL
from services.ai.exceptions import AIServiceUnavailableError
from services.ai.prompts.report_prompt import ReportPrompt
from services.ai.providers.base_provider import BaseProvider


class GeminiProvider(BaseProvider):

    MAX_RETRIES = 3

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

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

        for attempt in range(self.MAX_RETRIES):

            try:

                response = self.client.models.generate_content(
                    model=GEMINI_MODEL,
                    contents=prompt,
                )

                if not response.text:
                    raise AIServiceUnavailableError(
                        "The AI service returned an empty response."
                    )

                return response.text

            except ServerError as e:

                if attempt < self.MAX_RETRIES - 1:
                    time.sleep(2 ** attempt)
                    continue

                raise AIServiceUnavailableError(
                    "The AI service is temporarily experiencing high demand. Please try again in a few moments."
                ) from e

            except ClientError as e:

                raise AIServiceUnavailableError(
                    f"AI request failed: {e}"
                ) from e

            except AIServiceUnavailableError:
                raise

            except Exception as e:

                raise AIServiceUnavailableError(
                    "An unexpected error occurred while generating insights."
                ) from e