import streamlit as st

from .parser import ExecutiveParser
from .ui import ExecutiveUI


class ConfidenceSection:
    """
    Renders the Confidence Assessment section.
    """

    @staticmethod
    def render(content: str):

        content = ExecutiveParser.clean(content)

        ExecutiveUI.section(
            "Confidence Assessment",
            "📈",
        )

        if not content.strip():

            st.info(
                "No confidence assessment available."
            )

            return

        confidence = ConfidenceSection._parse(
            content
        )

        with st.container(border=True):

            ExecutiveUI.card(
                "Assessment"
            )

            ExecutiveUI.label(
                "Overall Confidence"
            )

            ExecutiveUI.badge(
                confidence["level"],
                ConfidenceSection._badge_color(
                    confidence["level"]
                ),
            )

            if confidence["reason"]:

                ExecutiveUI.divider()

                ExecutiveUI.label(
                    "Reason"
                )

                st.markdown(
                    confidence["reason"]
                )

            if confidence["limitations"]:

                ExecutiveUI.divider()

                ExecutiveUI.label(
                    "Data Limitations"
                )

                for limitation in confidence["limitations"]:

                    ExecutiveUI.bullet(
                        limitation
                    )

    @staticmethod
    def _parse(content):

        result = {
            "level": "Medium",
            "reason": "",
            "limitations": [],
        }

        current = None

        for line in content.splitlines():

            line = line.strip()

            if not line:
                continue

            lower = line.lower()

            if "overall confidence" in lower:

                current = "level"
                continue

            elif lower == "reason":

                current = "reason"
                continue

            elif "data limitation" in lower:

                current = "limitations"
                continue

            if current == "level":

                if any(
                    x in line.lower()
                    for x in [
                        "high",
                        "medium",
                        "low",
                    ]
                ):

                    result["level"] = line.strip()

            elif current == "reason":

                result["reason"] += line + " "

            elif current == "limitations":

                line = line.lstrip(
                    "-•* "
                ).strip()

                if line:

                    result["limitations"].append(
                        line
                    )

        result["reason"] = result[
            "reason"
        ].strip()

        return result

    @staticmethod
    def _badge_color(level):

        level = level.lower()

        if "high" in level:
            return "#22C55E"

        if "medium" in level:
            return "#F59E0B"

        if "low" in level:
            return "#EF4444"

        return "#64748B"