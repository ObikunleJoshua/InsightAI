import streamlit as st


class ExecutiveBrief:

    TITLES = {
        "Executive Decision Brief": "📋 Executive Decision Brief",
        "Key Findings": "🔍 Key Findings",
        "Business Impact": "💼 Business Impact",
        "Key Risks": "⚠️ Key Risks",
        "Recommended Actions": "🚀 Recommended Actions",
        "Questions for Leadership": "❓ Questions for Leadership",
        "Confidence Assessment": "📊 Confidence Assessment",
    }

    @staticmethod
    def render(response: str):

        if not response:
            st.warning("No analysis available.")
            return

        sections = ExecutiveBrief._parse(response)

        for title, content in sections.items():

            icon_title = ExecutiveBrief.TITLES.get(
                title,
                title,
            )

            with st.container(border=True):

                st.markdown(f"### {icon_title}")

                st.markdown(content)

    @staticmethod
    def _parse(text):

        sections = {}

        current = None

        buffer = []

        for line in text.splitlines():

            if line.startswith("# "):

                if current:

                    sections[current] = "\n".join(
                        buffer
                    ).strip()

                current = line.replace("# ", "").strip()

                buffer = []

            else:

                buffer.append(line)

        if current:

            sections[current] = "\n".join(
                buffer
            ).strip()

        return sections