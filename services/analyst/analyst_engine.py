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

        # Use the Intelligence Layer
        evidence = intelligence["evidence"]

        # Build AI Prompt
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

        # AI Response
        response = AIManager.generate_custom_prompt(
            prompt=prompt
        )

        return response