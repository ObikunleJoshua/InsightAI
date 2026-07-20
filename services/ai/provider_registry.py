from services.ai.providers.disabled_provider import DisabledProvider
from services.ai.providers.gemini_provider import GeminiProvider
from services.ai.providers.ollama_provider import OllamaProvider
from services.ai.providers.openai_provider import OpenAIProvider
from services.ai.providers.azure_provider import AzureProvider


class ProviderRegistry:
    """
    Central registry for all AI providers.

    This class is the single source of truth for:
    - Provider display names
    - Default models
    - Provider types (Cloud / Local / Disabled)
    - Provider implementation classes
    """

    PROVIDERS = {
        "disabled": {
            "name": "Disabled",
            "model": "-",
            "type": "disabled",
            "class": DisabledProvider,
        },

        "gemini": {
            "name": "Google Gemini",
            "model": "gemini-3.5-flash",
            "type": "cloud",
            "class": GeminiProvider,
        },

        "ollama": {
            "name": "Ollama",
            "model": "qwen3:4b",
            "type": "local",
            "class": OllamaProvider,
        },

        "openai": {
            "name": "OpenAI",
            "model": "gpt-4.1",
            "type": "cloud",
            "class": OpenAIProvider,
        },

        "azure": {
            "name": "Azure OpenAI",
            "model": "Azure GPT",
            "type": "cloud",
            "class": AzureProvider,
        },
    }

    @classmethod
    def get(cls, provider_key):
        """Return the provider metadata dictionary."""
        return cls.PROVIDERS.get(provider_key)

    @classmethod
    def get_provider_class(cls, provider_key):
        """Return the implementation class."""
        provider = cls.get(provider_key)

        if provider is None:
            return None

        return provider["class"]

    @classmethod
    def get_provider_name(cls, provider_key):
        """Return the display name."""
        provider = cls.get(provider_key)

        if provider is None:
            return "Unknown"

        return provider["name"]

    @classmethod
    def get_model(cls, provider_key):
        """Return the default model."""
        provider = cls.get(provider_key)

        if provider is None:
            return "-"

        return provider["model"]

    @classmethod
    def get_type(cls, provider_key):
        """Return the provider type."""
        provider = cls.get(provider_key)

        if provider is None:
            return "unknown"

        return provider["type"]

    @classmethod
    def get_provider_options(cls):
        """
        Returns a dictionary suitable for the sidebar selector.

        Example:
        {
            "Google Gemini": "gemini",
            "Ollama": "ollama",
            "Disabled": "disabled",
        }
        """
        return {
            data["name"]: key
            for key, data in cls.PROVIDERS.items()
            if key in ("gemini", "ollama", "disabled")
        }