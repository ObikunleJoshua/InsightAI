import re

from .parser import ExecutiveParser


class ExecutiveBriefRenderer:
    """
    Parses the AI Executive Decision Brief into sections.
    """

    SECTION_PATTERN = re.compile(
        r"^#\s+(.+?)\s*$",
        flags=re.MULTILINE,
    )

    @staticmethod
    def parse(report: str) -> dict:

        report = ExecutiveParser.clean(report)

        if not report:
            return {}

        matches = list(
            ExecutiveBriefRenderer.SECTION_PATTERN.finditer(
                report
            )
        )

        if not matches:
            return {
                "Executive Decision Brief": report
            }

        sections = {}

        for i, match in enumerate(matches):

            title = match.group(1).strip()

            start = match.end()

            end = (
                matches[i + 1].start()
                if i < len(matches) - 1
                else len(report)
            )

            body = report[start:end].strip()

            body = ExecutiveParser.clean(body)

            sections[title] = body

        return sections

    @staticmethod
    def get(
        sections: dict,
        section_name: str,
    ) -> str:

        value = sections.get(
            section_name,
            "",
        )

        return ExecutiveParser.clean(value)

    @staticmethod
    def has_section(
        sections: dict,
        section_name: str,
    ) -> bool:

        return bool(
            ExecutiveBriefRenderer.get(
                sections,
                section_name,
            )
        )