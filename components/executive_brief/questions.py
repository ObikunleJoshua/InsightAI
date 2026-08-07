import re
import streamlit as st

from .parser import ExecutiveParser
from .ui import ExecutiveUI


class LeadershipQuestionsSection:
    """
    Renders the Questions for Leadership section.
    """

    @staticmethod
    def render(content: str):

        content = ExecutiveParser.clean(content)

        ExecutiveUI.section(
            "Questions for Leadership",
            "❓",
        )

        if not content.strip():

            st.info(
                "No leadership questions available."
            )

            return

        questions = LeadershipQuestionsSection._parse(
            content
        )

        with st.container(border=True):

            ExecutiveUI.card(
                "Strategic Questions"
            )

            for question in questions:

                ExecutiveUI.question(
                    question
                )

    @staticmethod
    def _parse(content):

        questions = []

        for line in content.splitlines():

            line = line.strip()

            if not line:
                continue

            line = re.sub(
                r"^\d+\.\s*",
                "",
                line,
            )

            line = re.sub(
                r"^[-*•]\s*",
                "",
                line,
            )

            if (
                line
                and "questions for leadership"
                not in line.lower()
            ):

                questions.append(
                    line
                )

        return questions