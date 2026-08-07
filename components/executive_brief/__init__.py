from .renderer import ExecutiveBriefRenderer
from .snapshot import ExecutiveSnapshot
from .findings import FindingsSection
from .impact import BusinessImpactSection
from .risks import RiskSection
from .actions import ActionSection
from .questions import LeadershipQuestionsSection
from .confidence import ConfidenceSection
from .summary import ExecutiveSummarySection


class ExecutiveBrief:

    @staticmethod
    def render(response):

        from streamlit import session_state
        import streamlit as st

        sections = ExecutiveBriefRenderer.parse(response)

        quality = session_state.get(
            "dataset_quality",
            {},
        )

        persona = session_state.get(
            "ai_persona",
            "Executive Advisor",
        )

        context = session_state.get(
            "decision_context",
        )

        confidence_text = ExecutiveBriefRenderer.get(
            sections,
            "Confidence Assessment",
        )

        confidence = "Medium"

        if "high" in confidence_text.lower():
            confidence = "High"

        elif "low" in confidence_text.lower():
            confidence = "Low"

        ExecutiveSnapshot.render(
            decision_context=getattr(
                context,
                "context",
                "Unknown",
            ),
            persona=persona,
            quality=f'{quality.get("grade","N/A")} ({quality.get("score","N/A")}%)',
            confidence=confidence,
        )

        from .summary import ExecutiveSummarySection

        ExecutiveSummarySection.render(
            ExecutiveBriefRenderer.get(
                sections,
                "Executive Decision Brief",
            )
        )

        FindingsSection.render(
            ExecutiveBriefRenderer.get(
                sections,
                "Key Findings",
            )
        )

        BusinessImpactSection.render(
            ExecutiveBriefRenderer.get(
                sections,
                "Business Impact",
            )
        )

        RiskSection.render(
            ExecutiveBriefRenderer.get(
                sections,
                "Key Risks",
            )
        )

        ActionSection.render(
            ExecutiveBriefRenderer.get(
                sections,
                "Recommended Actions",
            )
        )

        LeadershipQuestionsSection.render(
            ExecutiveBriefRenderer.get(
                sections,
                "Questions for Leadership",
            )
        )

        ConfidenceSection.render(
            ExecutiveBriefRenderer.get(
                sections,
                "Confidence Assessment",
            )
        )