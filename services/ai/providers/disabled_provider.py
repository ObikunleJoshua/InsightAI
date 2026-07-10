from services.ai.providers.base_provider import BaseProvider


class DisabledProvider(BaseProvider):

    def generate_insights(
        self,
        dataset_type,
        profile,
        quality,
        kpis,
    ):

        return """
## AI Disabled

The AI engine is currently disabled.

To enable AI:

services/config.py

AI_PROVIDER = "ollama"
"""