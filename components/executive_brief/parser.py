import html
import re


class ExecutiveParser:
    """
    Cleans and normalizes AI output before rendering.
    """

    @staticmethod
    def clean(text: str) -> str:

        if not text:
            return ""

        # Normalize line endings
        text = text.replace("\r\n", "\n")

        # Decode HTML entities
        text = html.unescape(text)

        # Remove HTML tags
        text = re.sub(
            r"<[^>]+>",
            "",
            text,
            flags=re.DOTALL,
        )

        # Remove markdown separators
        text = re.sub(
            r"^[-=]{3,}$",
            "",
            text,
            flags=re.MULTILINE,
        )

        # Remove empty markdown emphasis
        text = text.replace("****", "")

        # Remove stray markdown bullets
        text = re.sub(
            r"^[•]\s*",
            "- ",
            text,
            flags=re.MULTILINE,
        )

        # Remove duplicate blank lines
        text = re.sub(
            r"\n{3,}",
            "\n\n",
            text,
        )

        # Strip trailing whitespace
        text = "\n".join(
            line.rstrip()
            for line in text.splitlines()
        )

        return text.strip()

    @staticmethod
    def lines(text: str):

        return [
            line.strip()
            for line in ExecutiveParser.clean(text).splitlines()
            if line.strip()
        ]

    @staticmethod
    def remove_markdown(text: str):

        text = ExecutiveParser.clean(text)

        text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
        text = re.sub(r"__(.*?)__", r"\1", text)
        text = re.sub(r"`(.*?)`", r"\1", text)

        return text.strip()