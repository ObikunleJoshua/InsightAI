import re
import streamlit as st

from .parser import ExecutiveParser
from .ui import ExecutiveUI


class FindingsSection:
    """
    Renders the Key Findings section.
    """

    @staticmethod
    def render(content: str):

        content = ExecutiveParser.clean(content)

        ExecutiveUI.section(
            "Key Findings",
            "🔍",
        )

        if not content.strip():

            st.info(
                "No findings available."
            )

            return

        findings = re.split(
            r"(?=### Finding\s+\d+)",
            content,
        )

        cards = []

        for finding in findings:

            finding = finding.strip()

            if not finding:
                continue

            cards.append(
                FindingsSection._parse(
                    finding
                )
            )

        for i in range(0, len(cards), 2):

            col1, col2 = st.columns(
                2,
                gap="large",
            )

            with col1:

                FindingsSection._card(
                    cards[i]
                )

            if i + 1 < len(cards):

                with col2:

                    FindingsSection._card(
                        cards[i + 1]
                    )

    @staticmethod
    def _parse(text):

        result = {
            "title": "Finding",
            "observation": "",
            "evidence": "",
            "interpretation": "",
        }

        current = None

        for line in text.splitlines():

            line = line.strip()

            if not line:
                continue

            if line.startswith("###"):

                result["title"] = (
                    line.replace(
                        "###",
                        "",
                    ).strip()
                )

                continue

            lower = line.lower()

            if lower.startswith("**observation") or lower == "observation":

                current = "observation"
                continue

            elif lower.startswith("**evidence") or lower == "evidence":

                current = "evidence"
                continue

            elif (
                lower.startswith("**business interpretation")
                or lower == "business interpretation"
            ):

                current = "interpretation"
                continue

            if current:

                result[current] += line + " "

        for key in result:

            if isinstance(result[key], str):

                result[key] = result[key].strip()

        return result

    @staticmethod
    def _card(item):

        with st.container(border=True):

            ExecutiveUI.card(
                item["title"]
            )

            sections = [
                (
                    "Observation",
                    item["observation"],
                ),
                (
                    "Evidence",
                    item["evidence"],
                ),
                (
                    "Business Interpretation",
                    item["interpretation"],
                ),
            ]

            first = True

            for title, body in sections:

                if not body:
                    continue

                if not first:

                    ExecutiveUI.divider()

                ExecutiveUI.label(
                    title
                )

                st.markdown(
                    body
                )

                first = False