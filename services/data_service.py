import pandas as pd


class DataService:
    """Handles loading and profiling datasets."""

    @staticmethod
    def load_dataset(uploaded_file):
        """Load CSV or Excel file into a DataFrame."""

        if uploaded_file.name.endswith(".csv"):
            return pd.read_csv(uploaded_file)

        elif uploaded_file.name.endswith(".xlsx"):
            return pd.read_excel(uploaded_file)

        else:
            raise ValueError("Unsupported file format.")

    @staticmethod
    def profile_dataset(df):
        """Generate a dataset profile."""

        profile = {}

        profile["rows"] = df.shape[0]
        profile["columns"] = df.shape[1]

        profile["missing_values"] = int(df.isnull().sum().sum())

        profile["duplicate_rows"] = int(df.duplicated().sum())

        profile["memory_usage_mb"] = round(
            df.memory_usage(deep=True).sum() / (1024 * 1024),
            2,
        )

        profile["numeric_columns"] = (
            df.select_dtypes(include="number")
            .columns.tolist()
        )

        profile["categorical_columns"] = (
            df.select_dtypes(include="object")
            .columns.tolist()
        )

        profile["date_columns"] = (
            df.select_dtypes(include="datetime")
            .columns.tolist()
        )

        return profile