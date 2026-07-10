from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Abstract base class for all AI providers.
    """

    @abstractmethod
    def generate_insights(
        self,
        dataset_type: dict,
        profile: dict,
        quality: dict,
        kpis: dict,
    ) -> str:
        """Generate AI insights."""
        pass