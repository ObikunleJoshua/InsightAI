import pandas as pd


class DataService:

    @staticmethod
    def load_dataset(uploaded_file):
        ...
        ...

    @staticmethod
    def profile_dataset(df):
        ...
        ...

    @staticmethod
    def calculate_quality_score(df):

        score = 100
        issues = []

        # Missing values
        missing = df.isnull().sum().sum()

        if missing > 0:
            score -= 10
            issues.append(
                f"{missing} missing values detected"
            )

        # Duplicate rows
        duplicates = df.duplicated().sum()

        if duplicates > 0:
            score -= 10
            issues.append(
                f"{duplicates} duplicate rows detected"
            )

        # Empty columns
        empty_columns = (
            df.columns[df.isnull().all()]
            .tolist()
        )

        if empty_columns:
            score -= 5
            issues.append(
                f"Empty columns: {empty_columns}"
            )

        score = max(score, 0)

        if score >= 90:
            quality = "Excellent"
        elif score >= 70:
            quality = "Good"
        elif score >= 50:
            quality = "Fair"
        else:
            quality = "Poor"

        return {
            "score": score,
            "quality": quality,
            "issues": issues,
        }