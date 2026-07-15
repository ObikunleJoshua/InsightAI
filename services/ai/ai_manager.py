from services.ai.config import AI_PROVIDER

from services.ai.providers.disabled_provider import DisabledProvider
from services.ai.providers.ollama_provider import OllamaProvider
from services.ai.providers.openai_provider import OpenAIProvider
from services.ai.providers.azure_provider import AzureProvider


class AIManager:
    """
    Routes AI requests to the configured provider.
    """

    PROVIDERS = {
        "disabled": DisabledProvider,
        "ollama": OllamaProvider,
        "openai": OpenAIProvider,
        "azure": AzureProvider,
    }

    @staticmethod
    def generate_insights(
        dataset_type,
        metadata,
        quality,
        kpis,
    ):

        provider_class = AIManager.PROVIDERS.get(AI_PROVIDER)

        if provider_class is None:
            raise ValueError(
                f"Unsupported AI provider: {AI_PROVIDER}"
            )

        provider = provider_class()

        return provider.generate_insights(
            dataset_type,
            metadata,
            quality,
            kpis,
        )