import pandas as pd


class DataService:
    """Handles dataset loading, profiling and quality checks."""

    @staticmethod
    def load_dataset(uploaded_file):
        """Load a CSV or Excel file."""

        if uploaded_file.name.endswith(".csv"):
            return pd.read_csv(uploaded_file)

        elif uploaded_file.name.endswith(".xlsx"):
            return pd.read_excel(uploaded_file)

        else:
            raise ValueError("Unsupported file format.")

    @staticmethod
    def profile_dataset(df):
        """Generate a profile of the dataset."""

        return {
            "rows": df.shape[0],
            "columns": df.shape[1],
            "missing_values": int(df.isnull().sum().sum()),
            "duplicate_rows": int(df.duplicated().sum()),
            "memory_usage_mb": round(
                df.memory_usage(deep=True).sum() / (1024 * 1024),
                2,
            ),
            "numeric_columns": df.select_dtypes(
                include="number"
            ).columns.tolist(),
            "categorical_columns": df.select_dtypes(
                include="object"
            ).columns.tolist(),
            "date_columns": df.select_dtypes(
                include="datetime"
            ).columns.tolist(),
        }

    @staticmethod
    def calculate_quality_score(df):
        """Calculate a simple dataset quality score."""

        score = 100
        issues = []

        missing = df.isnull().sum().sum()

        if missing > 0:
            score -= 10
            issues.append(
                f"{missing} missing values detected"
            )

        duplicates = df.duplicated().sum()

        if duplicates > 0:
            score -= 10
            issues.append(
                f"{duplicates} duplicate rows detected"
            )

        empty_columns = df.columns[df.isnull().all()].tolist()

        if empty_columns:
            score -= 5
            issues.append(
                f"Empty columns: {', '.join(empty_columns)}"
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