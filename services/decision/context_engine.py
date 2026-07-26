"""
Decision Context Engine

Determines the primary business decision context represented by a dataset.

The engine is deterministic and explainable. It evaluates dataset metadata
against the InsightAI Decision Context Knowledge Base and returns the
highest-confidence context together with supporting reasoning.
"""

from dataclasses import dataclass
from typing import List

from services.decision.contexts import DECISION_CONTEXTS


@dataclass
class DecisionContext:
    """
    Result returned by the Decision Context Engine.
    """

    context: str
    description: str
    confidence: float
    matched_keywords: List[str]
    primary_kpis: List[str]
    frameworks: List[str]


class DecisionContextEngine:
    """
    Decision Context Engine.

    Uses deterministic keyword matching to identify the most relevant
    business decision context for a dataset.
    """

    @staticmethod
    def analyze(columns: List[str]) -> DecisionContext:
        """
        Analyze dataset columns and determine the most appropriate
        decision context.

        Parameters
        ----------
        columns : List[str]
            Dataset column names.

        Returns
        -------
        DecisionContext
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

        if best_context is None:

            return DecisionContext(
                context="Unknown",
                description="No suitable decision context identified.",
                confidence=0.0,
                matched_keywords=[],
                primary_kpis=[],
                frameworks=[],
            )

        context = DECISION_CONTEXTS[best_context]

        confidence = (
            len(best_matches) / len(context["keywords"])
            if context["keywords"]
            else 0.0
        )

        return DecisionContext(
            context=best_context,
            description=context["description"],
            confidence=round(confidence, 2),
            matched_keywords=sorted(best_matches),
            primary_kpis=context["primary_kpis"],
            frameworks=context["frameworks"],
        )