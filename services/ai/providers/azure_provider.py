from services.ai.providers.base_provider import BaseProvider


class AzureProvider(BaseProvider):

    def generate_insights(
        self,
        dataset_type: dict,
        profile: dict,
        quality: dict,
        kpis: dict,
    ) -> str:

        return (
            "Azure OpenAI integration has not been implemented yet."
        )