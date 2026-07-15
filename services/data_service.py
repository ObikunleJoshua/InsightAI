import pandas as pd


class DataService:
    """Handles dataset loading and validation."""

    @staticmethod
    def load_dataset(uploaded_file):
        """Load a CSV or Excel file."""

        if uploaded_file.name.endswith(".csv"):
            return pd.read_csv(uploaded_file)

        elif uploaded_file.name.endswith(".xlsx"):
            return pd.read_excel(uploaded_file)

        else:
            raise ValueError("Unsupported file format.")