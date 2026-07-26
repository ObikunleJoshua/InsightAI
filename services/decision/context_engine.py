"""
Decision Context Engine

Determines the primary business decision context represented by a dataset.

The engine is deterministic and explainable. It evaluates dataset metadata
against the InsightAI Decision Context Knowledge Base and returns the
highest-confidence context together with supporting reasoning.
"""

from dataclasses import dataclass, field
from typing import List

from services.decision.contexts import DECISION_CONTEXTS


@dataclass
class DecisionContext:
    """
    Represents the complete decision context identified for a dataset.
    """

    # Detection
    context: str
    confidence: float

    # Explainability
    matched_keywords: List[str] = field(default_factory=list)

    # Knowledge
    description: str = ""
    business_objective: str = ""

    decision_priorities: List[str] = field(default_factory=list)
    executive_questions: List[str] = field(default_factory=list)

    primary_kpis: List[str] = field(default_factory=list)
    frameworks: List[str] = field(default_factory=list)

    recommended_visualizations: List[str] = field(default_factory=list)

    risk_indicators: List[str] = field(default_factory=list)

    strategic_focus: List[str] = field(default_factory=list)


class DecisionContextEngine:
    """
    Decision Context Engine.

    Uses deterministic keyword matching to identify the most relevant
    decision context for a dataset.
    """

    @staticmethod
    def analyze(columns: List[str]) -> DecisionContext:
        """
        Analyze dataset columns and determine the most appropriate
        decision context.
        """

        normalized_columns = [
            column.strip().lower()
            for column in columns
        ]

        best_context = None
        best_score = -1
        best_matches = []

        for context_name, context in DECISION_CONTEXTS.items():

            matches = []

            for keyword in context["keywords"]:
                if any(keyword in column for column in normalized_columns):
                    matches.append(keyword)

            score = len(matches)

            if score > best_score:
                best_score = score
                best_context = context_name
                best_matches = matches

        # No suitable context found
        if best_context is None:

            return DecisionContext(
                context="Unknown",
                confidence=0.0,

                matched_keywords=[],

                description="Unable to determine a suitable decision context.",

                business_objective="",

                decision_priorities=[],

                executive_questions=[],

                primary_kpis=[],

                frameworks=[],

                recommended_visualizations=[],

                risk_indicators=[],

                strategic_focus=[],
            )

        context = DECISION_CONTEXTS[best_context]

        confidence = (
            len(best_matches) / len(context["keywords"])
            if context["keywords"]
            else 0.0
        )

        return DecisionContext(
            context=best_context,
            confidence=round(confidence, 2),

            matched_keywords=sorted(best_matches),

            description=context["description"],
            business_objective=context["business_objective"],

            decision_priorities=context["decision_priorities"],

            executive_questions=context["executive_questions"],

            primary_kpis=context["primary_kpis"],

            frameworks=context["frameworks"],

            recommended_visualizations=context["recommended_visualizations"],

            risk_indicators=context["risk_indicators"],

            strategic_focus=context["strategic_focus"],
        )