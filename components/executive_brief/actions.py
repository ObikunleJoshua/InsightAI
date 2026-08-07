import re
import streamlit as st

from .parser import ExecutiveParser
from .ui import ExecutiveUI


class ActionSection:
    """
    Renders the Recommended Actions section.
    """

    @staticmethod
    def render(content: str):

        content = ExecutiveParser.clean(content)

        ExecutiveUI.section(
            "Recommended Actions",
            "🚀",
        )

        if not content.strip():

            st.info(
                "No recommendations available."
            )

            return

        sections = ActionSection._parse(
            content
        )

        col1, col2, col3 = st.columns(
            3,
            gap="large",
        )

        layout = [
            (
                col1,
                "⚡ Immediate",
                "Immediate",
            ),
            (
                col2,
                "📅 Medium-Term",
                "Medium-Term",
            ),
            (
                col3,
                "🎯 Strategic",
                "Strategic",
            ),
        ]

        for column, title, key in layout:

            with column:

                with st.container(border=True):

                    ExecutiveUI.card(
                        title
                    )

                    actions = sections.get(
                        key,
                        [],
                    )

                    if not actions:

                        st.caption(
                            "No actions identified."
                        )

                    else:

                        for action in actions:

                            ExecutiveUI.bullet(
                                action
                            )

    @staticmethod
    def _parse(content):

        sections = {
            "Immediate": [],
            "Medium-Term": [],
            "Strategic": [],
        }

        current = None

        for line in content.splitlines():

            line = line.strip()

            if not line:
                continue

            lower = line.lower()

            if "immediate" in lower:

                current = "Immediate"
                continue

            elif "medium" in lower:

                current = "Medium-Term"
                continue

            elif (
                "long" in lower
                or "strategic" in lower
            ):

                current = "Strategic"
                continue

            if current:

                line = re.sub(
                    r"^[-*•]\s*",
                    "",
                    line,
                )

                line = re.sub(
                    r"^\d+\.\s*",
                    "",
                    line,
                )

                line = line.strip()

                if line:

                    sections[current].append(
                        line
                    )

        return sections