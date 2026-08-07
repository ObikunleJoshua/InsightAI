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
        dataset_type,
        metadata,
        quality,
        kpis,
        persona,
        analysis_objective,
    ) -> str:

        prompt = ReportPrompt.build(
            dataset_type=dataset_type,
            metadata=metadata,
            quality=quality,
            kpis=kpis,
            persona=persona,
            analysis_objective=analysis_objective,
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

                message = str(e)

                if "RESOURCE_EXHAUSTED" in message or "429" in message:
                    raise AIServiceUnavailableError(
                        "Gemini API quota exceeded.\n\n"
                        "Please wait a minute and try again, or use another API key if your daily free quota has been exhausted."
                    )

                raise AIServiceUnavailableError(
                    f"AI request failed: {e}"
                ) from e

            except AIServiceUnavailableError:
                raise

            except Exception as e:

                raise AIServiceUnavailableError(
                    "An unexpected error occurred while generating insights."
                ) from e


    def generate_from_prompt(
        self,
        prompt: str,
    ) -> str:
        """
        Generates a response from a pre-built prompt.
        """

        print("=" * 80)
        print("GEMINI REQUEST STARTED")
        print(f"Prompt length: {len(prompt)} characters")
        print("=" * 80)

        for attempt in range(self.MAX_RETRIES):

            try:

                print(f"Attempt {attempt + 1}...")

                response = self.client.models.generate_content(
                    model=GEMINI_MODEL,
                    contents=prompt,
                )

                print("Gemini returned a response.")

                if not response.text:
                    raise AIServiceUnavailableError(
                        "The AI service returned an empty response."
                    )

                print(f"Response length: {len(response.text)} characters")
                print("GEMINI REQUEST FINISHED")
                print("=" * 80)

                return response.text

            except ServerError as e:

                print(f"ServerError: {e}")

                if attempt < self.MAX_RETRIES - 1:
                    time.sleep(2 ** attempt)
                    continue

                raise AIServiceUnavailableError(
                    "The AI service is temporarily experiencing high demand. Please try again in a few moments."
                ) from e

            except ClientError as e:

                print(f"ClientError: {e}")

                raise AIServiceUnavailableError(
                    f"AI request failed: {e}"
                ) from e

            except Exception as e:

                print(f"Unexpected Exception: {repr(e)}")

                raise AIServiceUnavailableError(
                    "An unexpected error occurred while generating insights."
                ) from e