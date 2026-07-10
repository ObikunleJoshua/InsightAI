from services.ai.config import AI_PROVIDER

from services.ai.providers.disabled_provider import DisabledProvider
from services.ai.providers.ollama_provider import OllamaProvider


class AIManager:
    """Routes AI requests to the configured provider."""

    @staticmethod
    def generate_insights(dataset_type, profile, quality, kpis):

        if AI_PROVIDER == "disabled":
            provider = DisabledProvider()

        elif AI_PROVIDER == "ollama":
            provider = OllamaProvider()

        else:
            raise ValueError(
                f"Unsupported AI provider: {AI_PROVIDER}"
            )

        return provider.generate_insights(
            dataset_type,
            profile,
            quality,
            kpis,
        )