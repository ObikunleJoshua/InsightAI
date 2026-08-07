import streamlit as st

from .parser import ExecutiveParser
from .ui import ExecutiveUI


class ExecutiveSummarySection:

    @staticmethod
    def render(content: str):

        content = ExecutiveParser.clean(content)

        if not content.strip():
            return

        ExecutiveUI.section(
            "Executive Decision Brief",
            "📋",
        )

        paragraphs = [
            p.strip()
            for p in content.split("\n\n")
            if p.strip()
        ]

        for paragraph in paragraphs:
            st.markdown(paragraph)

            ExecutiveUI.spacer(12)