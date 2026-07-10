from services.ai.providers.base_provider import BaseProvider


class OpenAIProvider(BaseProvider):

    def generate_insights(
        self,
        dataset_type: dict,
        profile: dict,
        quality: dict,
        kpis: dict,
    ) -> str:

        return (
            "OpenAI integration has not been implemented yet."
        )