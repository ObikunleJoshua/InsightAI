from services.analyst.evidence_builder import EvidenceBuilder
from services.ai.prompts.analyst_prompt import AnalystPrompt


class AnalystEngine:
    """
    Coordinates the AI Business Analyst workflow.
    """

    @staticmethod
    def prepare_analysis(
        df,
        dataset_type,
        metadata,
        quality,
        kpis,
        decision_context,
        persona,
        analysis_objective,
        business_question,
    ):

        evidence = EvidenceBuilder.build(df)

        prompt = AnalystPrompt.build(
            dataset_type=dataset_type,
            metadata=metadata,
            quality=quality,
            kpis=kpis,
            decision_context=decision_context,
            persona=persona,
            analysis_objective=analysis_objective,
            business_question=business_question,
        )

        return {

            "prompt": prompt,

            "evidence": evidence,

            "question": business_question,

            "context": decision_context.context,
        }