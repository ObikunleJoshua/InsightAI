from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Abstract base class for all AI providers.
    """

    @abstractmethod
    def generate_insights(
        self,
        dataset_type,
        profile,
        quality,
        kpis,
    ):
        """Generate AI insights."""
        pass