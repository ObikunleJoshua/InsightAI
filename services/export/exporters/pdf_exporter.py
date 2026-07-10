from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

from services.export.exporters.base_exporter import BaseExporter


class PDFExporter(BaseExporter):
    """
    Exports reports as PDF documents.
    """

    EXPORT_FOLDER = Path("exports")

    def export(self, report: str, filename: str) -> str:

        self.EXPORT_FOLDER.mkdir(exist_ok=True)

        file_path = self.EXPORT_FOLDER / f"{filename}.pdf"

        document = SimpleDocTemplate(str(file_path))

        styles = getSampleStyleSheet()

        story = [
            Paragraph("<b>InsightAI Report</b>", styles["Heading1"]),
            Paragraph(report.replace("\n", "<br/>"), styles["BodyText"]),
        ]

        document.build(story)

        return str(file_path)