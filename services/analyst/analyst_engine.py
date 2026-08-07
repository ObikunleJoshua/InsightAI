from services.analyst.evidence_builder import EvidenceBuilder
from services.ai.ai_manager import AIManager
from services.ai.prompts.analyst_prompt import AnalystPrompt


class AnalystEngine:
    """
    Orchestrates the AI Business Analyst workflow.
    """

    @staticmethod
    def analyze(
        df,
        dataset_type,
        metadata,
        quality,
        kpis,
        intelligence,
        decision_context,
        persona,
        analysis_objective,
        business_question,
    ):

        # Build business evidence
        evidence = EvidenceBuilder.build(df)

        # Build AI prompt
        prompt = AnalystPrompt.build(
            dataset_type=dataset_type,
            metadata=metadata,
            quality=quality,
            kpis=kpis,
            decision_context=decision_context,
            evidence=evidence,
            persona=persona,
            analysis_objective=analysis_objective,
            business_question=business_question,
        )

        # -------------------------
        # Validation
        # -------------------------

        if prompt is None:
            raise ValueError("AnalystPrompt.build() returned None.")

        if not isinstance(prompt, str):
            raise ValueError(
                f"Prompt must be a string. Got {type(prompt)}"
            )

        if len(prompt.strip()) == 0:
            raise ValueError(
                "Prompt is empty."
            )

        # -------------------------
        # Generate AI response
        # -------------------------

        return AIManager.generate_custom_prompt(
            prompt=prompt
        )