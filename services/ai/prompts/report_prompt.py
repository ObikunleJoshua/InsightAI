from services.ai.personas import PERSONAS


class ReportPrompt:
    """
    Builds prompts for AI-generated Executive Briefings.
    """

    @staticmethod
    def build(
        dataset_type,
        metadata,
        quality,
        kpis,
        persona,
        analysis_objective,
    ):

        info = metadata["dataset_info"]
        capabilities = metadata["capabilities"]

        persona_info = PERSONAS.get(
            persona,
            {},
        )

        persona_description = persona_info.get(
            "description",
            "",
        )

        primary_goal = persona_info.get(
            "primary_goal",
            "",
        )

        communication_style = persona_info.get(
            "communication_style",
            "",
        )

        priorities = ", ".join(
            persona_info.get(
                "priorities",
                [],
            )
        )

        focus_questions = ", ".join(
            persona_info.get(
                "focus_questions",
                [],
            )
        )

        prompt = f"""
You are an experienced {persona}.

{persona_description}

Primary Goal:
{primary_goal}

Communication Style:
{communication_style}

Business Priorities:
{priorities}

Executive Focus:
{focus_questions}

----------------------------------------------------

ANALYSIS OBJECTIVE

{analysis_objective}

----------------------------------------------------

DATASET TYPE

{dataset_type["label"]}

----------------------------------------------------

DATASET INFORMATION

Rows:
{info["rows"]}

Columns:
{info["columns"]}

Duplicate Rows:
{info["duplicate_rows"]}

Memory Usage:
{info["memory_usage_mb"]} MB

----------------------------------------------------

DATA QUALITY

Score:
{quality["score"]}%

Grade:
{quality["grade"]}

Warnings:
{quality["warnings"]}

----------------------------------------------------

DATASET CAPABILITIES

Numeric Columns:
{len(capabilities["numeric_columns"])}

Categorical Columns:
{len(capabilities["categorical_columns"])}

Datetime Columns:
{len(capabilities["datetime_columns"])}

Text Columns:
{len(capabilities["text_columns"])}

----------------------------------------------------

BUSINESS KPIs

{kpis}

----------------------------------------------------

Instructions

Prepare an executive-quality business briefing.

Use ONLY the information provided.

Do NOT invent numbers.

If the available evidence is insufficient, clearly state that additional analysis is required.

Respond using exactly this structure:

MEMORANDUM

TO:
Chief Executive Officer and Executive Board

FROM:
{persona}

SUBJECT:
Executive Performance & Strategic Direction

----------------------------------------------------

1. Executive Summary

Provide a concise executive overview.

----------------------------------------------------

2. Three Key Findings

Provide three findings.

For each finding, explain why it matters.

----------------------------------------------------

3. Three Strategic Recommendations

Provide three practical recommendations.

For each recommendation, include a short Business Implication.

Keep the response under 600 words.

Write professionally for executive leadership.
"""

        return prompt[:7000]