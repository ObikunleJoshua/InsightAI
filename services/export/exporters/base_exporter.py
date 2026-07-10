from abc import ABC, abstractmethod


class BaseExporter(ABC):
    """
    Abstract base class for all report exporters.
    """

    @abstractmethod
    def export(self, report: str, filename: str) -> str:
        """
        Export the report.

        Args:
            report: The report content.
            filename: Output filename (without extension).

        Returns:
            Path to the exported file.
        """
        pass