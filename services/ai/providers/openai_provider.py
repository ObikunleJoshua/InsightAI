from services.ai.providers.base_provider import BaseProvider


class OpenAIProvider(BaseProvider):

    def generate_insights(
        self,
        dataset_type,
        profile,
        quality,
        kpis,
    ):

        return (
            "OpenAI integration has not been implemented yet."
        )