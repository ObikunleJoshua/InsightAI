import pandas as pd
import numpy as np


class AnalyticsService:
    """
    Performs advanced statistical analysis on datasets.
    """

    @staticmethod
    def get_numeric_data(df: pd.DataFrame) -> pd.DataFrame:
        """
        Return only numeric columns.
        """
        return df.select_dtypes(include="number")

    @staticmethod
    def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
        """
        Generate a Pearson correlation matrix for numeric columns.
        """

        numeric_df = AnalyticsService.get_numeric_data(df)

        if numeric_df.shape[1] < 2:
            return pd.DataFrame()

        return numeric_df.corr().round(2)

    @staticmethod
    def detect_outliers(df: pd.DataFrame) -> dict:
        """
        Detect outliers in numeric columns using the IQR method.
        """

        numeric_df = AnalyticsService.get_numeric_data(df)

        results = {}

        for column in numeric_df.columns:

            q1 = numeric_df[column].quantile(0.25)
            q3 = numeric_df[column].quantile(0.75)

            iqr = q3 - q1

            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr

            outliers = numeric_df[
                (numeric_df[column] < lower)
                | (numeric_df[column] > upper)
            ]

            results[column] = len(outliers)

        return results

    @staticmethod
    def get_numeric_columns(df: pd.DataFrame) -> list:
        """
        Return all numeric column names.
        """

        numeric_df = AnalyticsService.get_numeric_data(df)

        return numeric_df.columns.tolist()

    @staticmethod
    def calculate_insight_score(
        df: pd.DataFrame,
        quality: dict,
    ) -> dict:
        """
        Calculate the overall Insight Score.
        """

        score = 0

        # ----------------------
        # Data Quality (40)
        # ----------------------

        score += (quality["score"] / 100) * 40

        # ----------------------
        # Numeric Columns (20)
        # ----------------------

        numeric_columns = len(
            AnalyticsService.get_numeric_columns(df)
        )

        score += min(numeric_columns, 5) * 4

        # ----------------------
        # Dataset Size (20)
        # ----------------------

        rows = len(df)

        if rows >= 1000:
            score += 20
        elif rows >= 500:
            score += 15
        elif rows >= 100:
            score += 10
        else:
            score += 5

        # ----------------------
        # Missing Values (20)
        # ----------------------

        missing = int(df.isnull().sum().sum())

        if missing == 0:
            score += 20
        elif missing <= 10:
            score += 15
        elif missing <= 50:
            score += 10
        else:
            score += 5

        score = round(score)

        if score >= 90:
            rating = "★★★★★"

        elif score >= 80:
            rating = "★★★★☆"

        elif score >= 70:
            rating = "★★★☆☆"

        elif score >= 60:
            rating = "★★☆☆☆"

        else:
            rating = "★☆☆☆☆"

        return {
            "score": score,
            "rating": rating,
            "breakdown": {
                "Data Quality": round((quality["score"] / 100) * 40),
                "Numeric Columns": min(numeric_columns, 5) * 4,
                "Dataset Size": (
                    20 if rows >= 1000
                    else 15 if rows >= 500
                    else 10 if rows >= 100
                    else 5
                ),
                "Missing Values": (
                    20 if missing == 0
                    else 15 if missing <= 10
                    else 10 if missing <= 50
                    else 5
                ),
            },
        }