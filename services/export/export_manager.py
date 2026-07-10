from services.export.exporters.markdown_exporter import MarkdownExporter
from services.export.exporters.docx_exporter import DocxExporter
from services.export.exporters.pdf_exporter import PDFExporter


class ExportManager:
    """
    Routes report export requests to the appropriate exporter.
    """

    EXPORTERS = {
        "markdown": MarkdownExporter,
        "docx": DocxExporter,
        "pdf": PDFExporter,
    }

    @staticmethod
    def export(report: str, filename: str, file_type: str) -> str:

        exporter_class = ExportManager.EXPORTERS.get(file_type.lower())

        if exporter_class is None:
            raise ValueError(f"Unsupported export type: {file_type}")

        exporter = exporter_class()

        return exporter.export(report, filename)