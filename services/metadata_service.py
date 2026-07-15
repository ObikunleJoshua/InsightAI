import pandas as pd
from pandas.api.types import (
    is_numeric_dtype,
    is_datetime64_any_dtype,
    is_bool_dtype,
)


class MetadataService:
    """Builds the Dataset Intelligence object."""

    @staticmethod
    def build(df: pd.DataFrame) -> dict:
        dataset_info = MetadataService._dataset_info(df)
        capabilities = MetadataService._capabilities(df)

        return {
            # Legacy keys (v1.0 compatibility)
            "rows": dataset_info["rows"],
            "columns": dataset_info["columns"],
            "missing_values": int(df.isnull().sum().sum()),
            "duplicate_rows": dataset_info["duplicate_rows"],
            "memory_usage_mb": dataset_info["memory_usage_mb"],
            "numeric_columns": capabilities["numeric_columns"],
            "categorical_columns": capabilities["categorical_columns"],
            "date_columns": capabilities["datetime_columns"],

            # New architecture
            "dataset_info": dataset_info,
            "schema": MetadataService._schema(df),
            "columns_profiles": MetadataService._column_metadata(df),
            "quality": MetadataService._quality(df),
            "capabilities": capabilities,
        }

    @staticmethod
    def _dataset_info(df):
        memory = df.memory_usage(deep=True).sum()

        return {
            "rows": len(df),
            "columns": len(df.columns),
            "memory_usage_bytes": int(memory),
            "memory_usage_mb": round(memory / (1024 ** 2), 2),
            "duplicate_rows": int(df.duplicated().sum()),
        }

    @staticmethod
    def _schema(df):
        return {
            "column_order": list(df.columns),
            "index_name": df.index.name,
            "primary_key_candidate": None,
        }

    @staticmethod
    def _column_metadata(df):
        columns = []

        for column in df.columns:
            series = df[column]
            unique = int(series.nunique(dropna=True))

            columns.append(
                {
                    "name": column,
                    "dtype": str(series.dtype),
                    "category": MetadataService._column_category(series),
                    "missing": int(series.isna().sum()),
                    "missing_percent": round(
                        (series.isna().sum() / len(df)) * 100, 2
                    )
                    if len(df)
                    else 0,
                    "unique": unique,
                    "cardinality": MetadataService._cardinality(unique),
                    "sample_values": series.dropna()
                    .head(5)
                    .tolist(),
                }
            )

        return columns

    @staticmethod
    def _quality(df):
        score = 100
        warnings = []

        missing = int(df.isna().sum().sum())
        duplicates = int(df.duplicated().sum())

        if missing:
            score -= 10
            warnings.append(f"{missing} missing values detected")

        if duplicates:
            score -= 10
            warnings.append(f"{duplicates} duplicate rows detected")

        score = max(score, 0)

        if score >= 90:
            grade = "Excellent"
        elif score >= 70:
            grade = "Good"
        elif score >= 50:
            grade = "Fair"
        else:
            grade = "Poor"

        return {
            "score": score,
            "quality": grade,   # Temporary for backward compatibility
            "grade": grade,
            "issues": warnings, 
            "warnings": warnings,
        }

    @staticmethod
    def _capabilities(df):
        numeric = []
        categorical = []
        datetime = []
        boolean = []
        text = []

        for column in df.columns:
            series = df[column]

            if is_numeric_dtype(series):
                numeric.append(column)
            elif is_datetime64_any_dtype(series):
                datetime.append(column)
            elif is_bool_dtype(series):
                boolean.append(column)
            elif str(series.dtype) == "category":
                categorical.append(column)
            else:
                text.append(column)

        return {
            "numeric_columns": numeric,
            "categorical_columns": categorical,
            "datetime_columns": datetime,
            "boolean_columns": boolean,
            "text_columns": text,
            "supports_correlation": len(numeric) >= 2,
            "supports_groupby": len(categorical) + len(text) > 0,
            "supports_time_series": len(datetime) > 0,
            "supports_outlier_detection": len(numeric) > 0,
        }

    @staticmethod
    def _column_category(series):
        if is_numeric_dtype(series):
            return "numeric"

        if is_datetime64_any_dtype(series):
            return "datetime"

        if is_bool_dtype(series):
            return "boolean"

        if str(series.dtype) == "category":
            return "categorical"

        return "text"

    @staticmethod
    def _cardinality(unique):
        if unique <= 10:
            return "low"

        if unique <= 100:
            return "medium"

        return "high"