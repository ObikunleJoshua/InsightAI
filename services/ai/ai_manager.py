import streamlit as st

from services.ai.config import AI_PROVIDER
from services.ai.provider_registry import ProviderRegistry


class AIManager:
    """
    Routes AI requests to the configured provider.
    """

    @staticmethod
    def generate_insights(
        dataset_type,
        metadata,
        quality,
        kpis,
    ):

        provider_name = st.session_state.get(
            "ai_provider",
            AI_PROVIDER,
        )

        provider_class = ProviderRegistry.get_provider_class(
            provider_name
        )

        if provider_class is None:
            raise ValueError(
                f"Unsupported AI provider: {provider_name}"
            )

        provider = provider_class()

        return provider.generate_insights(
            dataset_type,
            metadata,
            quality,
            kpis,
        )