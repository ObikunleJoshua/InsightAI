import streamlit as st

from .parser import ExecutiveParser
from .ui import ExecutiveUI


class BusinessImpactSection:
    """
    Renders the Business Impact section.
    """

    @staticmethod
    def render(content: str):

        content = ExecutiveParser.clean(content)

        ExecutiveUI.section(
            "Business Impact",
            "📊",
        )

        if not content.strip():

            st.info(
                "No business impact available."
            )

            return

        impacts = BusinessImpactSection._parse(
            content
        )

        for i in range(0, len(impacts), 2):

            col1, col2 = st.columns(
                2,
                gap="large",
            )

            with col1:

                BusinessImpactSection._card(
                    impacts[i]
                )

            if i + 1 < len(impacts):

                with col2:

                    BusinessImpactSection._card(
                        impacts[i + 1]
                    )

    @staticmethod
    def _parse(content):

        sections = []

        current_title = None
        current_body = []

        for line in content.splitlines():

            line = line.strip()

            if not line:
                continue

            if line.startswith("###"):

                if current_title:

                    sections.append(
                        {
                            "title": current_title,
                            "body": " ".join(current_body).strip(),
                        }
                    )

                current_title = (
                    line.replace(
                        "###",
                        "",
                    ).strip()
                )

                current_body = []

            else:

                current_body.append(
                    line
                )

        if current_title:

            sections.append(
                {
                    "title": current_title,
                    "body": " ".join(current_body).strip(),
                }
            )

        return sections

    @staticmethod
    def _card(item):

        with st.container(border=True):

            ExecutiveUI.card(
                item["title"]
            )

            st.markdown(
                item["body"]
            )