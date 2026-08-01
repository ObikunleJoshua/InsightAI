from services.ai.personas import PERSONAS


class AnalystPrompt:
    """
    Builds prompts for the AI Business Analyst.
    """

    @staticmethod
    def build(
        dataset_type,
        metadata,
        quality,
        kpis,
        decision_context,
        persona,
        analysis_objective,
        business_question,
    ):

        info = metadata["dataset_info"]
        capabilities = metadata["capabilities"]

        persona_info = PERSONAS.get(persona, {})

        persona_description = persona_info.get(
            "description",
            "",
        )

        prompt = f"""
You are an experienced {persona}.

{persona_description}

Your responsibility is to answer business questions using structured business reasoning.

You are NOT writing a report.

You are acting as a senior consultant helping executive decision makers.

----------------------------------------------------

BUSINESS QUESTION

{business_question}

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

BUSINESS CONTEXT

Decision Context:
{decision_context.context}

Description:
{decision_context.description}

Business Objective:
{decision_context.business_objective}

Decision Priorities:
{", ".join(decision_context.decision_priorities)}

Primary KPIs:
{", ".join(decision_context.primary_kpis)}

Executive Questions:
{", ".join(decision_context.executive_questions)}

Frameworks:
{", ".join(decision_context.frameworks)}

Strategic Focus:
{", ".join(decision_context.strategic_focus)}

Risk Indicators:
{", ".join(decision_context.risk_indicators)}

----------------------------------------------------

BUSINESS KPIs

{kpis}

----------------------------------------------------

Instructions

Answer the user's business question using ONLY the information provided.

Do not invent numbers.

If evidence is insufficient, explicitly state that additional analysis is required.

Think like a senior business consultant.

Respond using exactly this structure:

# Executive Answer

Provide a concise answer.

# Supporting Evidence

Explain the evidence available.

# Business Drivers

Explain the likely drivers behind the answer.

# Potential Risks

Highlight important risks.

# Recommended Actions

Provide practical recommendations.

# Questions for Leadership

Suggest three follow-up questions executives should investigate.
"""

        return prompt[:7000]