from services.ai.personas import PERSONAS
from services.intelligence.evidence_formatter import EvidenceFormatter


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
        evidence,
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

        formatted_evidence = EvidenceFormatter.format(
            evidence
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

BUSINESS INTELLIGENCE

{formatted_evidence}

----------------------------------------------------

Instructions

You are preparing an Executive Decision Brief for senior leadership.

Your response must be professional, evidence-based, concise, and action-oriented.

Use ONLY the information available in the dataset, KPIs, business context, and business intelligence provided.

Never invent numbers, facts, trends, or relationships.

If there is insufficient evidence to answer part of the question, explicitly state that additional analysis or data is required.

Always distinguish:
- Facts supported by the dataset.
- Reasonable business inferences.
- Recommendations.

Respond using EXACTLY the following structure:

# Executive Decision Brief

Write a concise 3–5 sentence executive summary that answers the business question and states your primary recommendation.

---

# Key Findings

Provide 4–6 bullet points highlighting the most important findings supported by the available evidence.

---

# Business Impact

Explain the likely impact of these findings on:
- Financial Performance
- Operations
- Customers
- Business Growth

Only discuss areas supported by the available evidence.

---

# Key Risks

List the major business risks.

For each risk, indicate:
- Risk Level (High, Medium, or Low)
- Why it matters

---

# Recommended Actions

Organize recommendations into:

## Immediate Actions (Next 30 Days)

## Medium-Term Actions (30–90 Days)

## Strategic Initiatives (Beyond 90 Days)

Recommendations must be practical, prioritized, and supported by the available evidence.

---

# Questions for Leadership

Suggest five strategic questions leadership should investigate next.

---

# Confidence Assessment

State:
- Confidence Level (High, Medium, or Low)
- Why this confidence level was assigned
- Any important data limitations
"""

        return prompt[:7000]