class ReportPrompt:
    """Builds prompts for AI-generated reports."""

    @staticmethod
    def build(dataset_type, metadata, quality, kpis):

        info = metadata["dataset_info"]
        capabilities = metadata["capabilities"]

        prompt = f"""
You are a Senior Data Intelligence Analyst.

Analyze the following dataset metadata.

Dataset Type:
{dataset_type["label"]}

Dataset Information:
- Rows: {info["rows"]}
- Columns: {info["columns"]}
- Duplicate Rows: {info["duplicate_rows"]}
- Memory Usage: {info["memory_usage_mb"]} MB

Data Quality:
- Score: {quality["score"]}%
- Grade: {quality["grade"]}
- Warnings: {quality["warnings"]}

Dataset Capabilities:
- Numeric Columns: {len(capabilities["numeric_columns"])}
- Categorical Columns: {len(capabilities["categorical_columns"])}
- Datetime Columns: {len(capabilities["datetime_columns"])}
- Text Columns: {len(capabilities["text_columns"])}

Business KPIs:
{kpis}

Write:

1. Executive Summary

2. Three Key Findings

3. Three Recommendations

Rules:
- Keep the response under 300 words.
- Be professional.
- Do NOT invent numbers.
- Use only the information provided.
"""

        return prompt[:3000]