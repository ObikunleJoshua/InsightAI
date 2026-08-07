import re
import streamlit as st

from .parser import ExecutiveParser
from .ui import ExecutiveUI


class RiskSection:
    """
    Renders the Key Risks section.
    """

    @staticmethod
    def render(content: str):

        content = ExecutiveParser.clean(content)

        ExecutiveUI.section(
            "Key Risks",
            "⚠️",
        )

        if not content.strip():

            st.info(
                "No business risks identified."
            )

            return

        risks = re.split(
            r"(?=### Risk\s+\d+)",
            content,
        )

        cards = []

        for risk in risks:

            risk = risk.strip()

            if not risk:
                continue

            cards.append(
                RiskSection._parse(
                    risk
                )
            )

        for i in range(0, len(cards), 2):

            col1, col2 = st.columns(
                2,
                gap="large",
            )

            with col1:

                RiskSection._card(
                    cards[i]
                )

            if i + 1 < len(cards):

                with col2:

                    RiskSection._card(
                        cards[i + 1]
                    )

    @staticmethod
    def _parse(text):

        result = {
            "title": "Business Risk",
            "level": "Not Assessed",
            "description": "",
            "impact": "",
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

            if lower.startswith("**level") or lower == "level":

                current = "level"
                continue

            elif lower.startswith("**description") or lower == "description":

                current = "description"
                continue

            elif (
                lower.startswith("**why")
                or lower.startswith("**business impact")
                or lower == "why it matters"
            ):

                current = "impact"
                continue

            if current == "level":

                result["level"] = line.strip()

            elif current == "description":

                result["description"] += line + " "

            elif current == "impact":

                result["impact"] += line + " "

        result["description"] = result["description"].strip()
        result["impact"] = result["impact"].strip()

        return result

    @staticmethod
    def _card(item):

        with st.container(border=True):

            level = item["level"].lower()

            if "high" in level:

                ExecutiveUI.badge(
                    "HIGH",
                    "#EF4444",
                )

            elif "medium" in level:

                ExecutiveUI.badge(
                    "MEDIUM",
                    "#F59E0B",
                )

            elif "low" in level:

                ExecutiveUI.badge(
                    "LOW",
                    "#22C55E",
                )

            else:

                ExecutiveUI.badge(
                    "NOT ASSESSED",
                    "#64748B",
                )

            ExecutiveUI.spacer(8)

            ExecutiveUI.card(
                item["title"]
            )

            if item["description"]:

                ExecutiveUI.label(
                    "Description"
                )

                st.markdown(
                    item["description"]
                )

            if item["impact"]:

                ExecutiveUI.divider()

                ExecutiveUI.label(
                    "Business Impact"
                )

                st.markdown(
                    item["impact"]
                )