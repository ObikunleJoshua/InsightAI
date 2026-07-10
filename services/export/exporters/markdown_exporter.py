from pathlib import Path

from services.export.exporters.base_exporter import BaseExporter


class MarkdownExporter(BaseExporter):
    """
    Exports reports as Markdown files.
    """

    EXPORT_FOLDER = Path("exports")

    def export(self, report: str, filename: str) -> str:
        """
        Export report to a Markdown (.md) file.
        """

        self.EXPORT_FOLDER.mkdir(exist_ok=True)

        file_path = self.EXPORT_FOLDER / f"{filename}.md"

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(report)

        return str(file_path)