class ReportPrompt:
    """Builds prompts for AI-generated business intelligence reports."""

    @staticmethod
    def build(dataset_type, profile, quality, kpis):

        prompt = f"""
You are a Senior Business Intelligence Analyst.

Analyze the following dataset summary.

Dataset Type:
{dataset_type["label"]}

Quality Score:
{quality["score"]}%

Rows:
{profile["rows"]}

Columns:
{profile["columns"]}

Missing Values:
{profile["missing_values"]}

KPIs:
{kpis}

Write:

1. Executive Summary

2. Three Key Findings

3. Three Recommendations

Keep the response under 300 words.

Keep the report professional.

Do NOT invent numbers.

Use only the information provided.
"""

        return prompt[:3000]