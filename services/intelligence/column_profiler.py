import pandas as pd

from pandas.api.types import (
    is_numeric_dtype,
    is_datetime64_any_dtype,
    is_string_dtype,
)


class ColumnProfiler:
    """
    Produces factual metadata about every column.

    This class NEVER performs business reasoning.
    It only reports observable facts.
    """

    @staticmethod
    def profile(df: pd.DataFrame):

        profiles = []

        total_rows = max(len(df), 1)

        for column in df.columns:

            series = df[column]

            non_null = series.dropna()

            profile = {

                "column": column,

                "dtype": str(series.dtype),

                "rows": len(series),

                "null_count": int(series.isna().sum()),

                "null_ratio": round(
                    series.isna().mean(),
                    4,
                ),

                "unique_values": int(
                    non_null.nunique()
                ),

                "unique_ratio": round(
                    non_null.nunique() / total_rows,
                    4,
                ),

                "is_numeric": bool(
                    is_numeric_dtype(series)
                ),

                "is_datetime": bool(
                    is_datetime64_any_dtype(series)
                ),

                "is_text": bool(
                    is_string_dtype(series)
                ),

                "sample_values": non_null.head(5).tolist(),
            }

            # Numeric statistics

            if profile["is_numeric"] and not non_null.empty:

                profile["statistics"] = {

                    "min": float(non_null.min()),

                    "max": float(non_null.max()),

                    "mean": float(non_null.mean()),

                    "median": float(non_null.median()),

                    "std": float(non_null.std())
                    if len(non_null) > 1
                    else 0.0,
                }

            else:

                profile["statistics"] = None

            # Text statistics

            if profile["is_text"] and not non_null.empty:

                lengths = non_null.astype(str).str.len()

                profile["average_length"] = round(
                    lengths.mean(),
                    2,
                )

            else:

                profile["average_length"] = None

            profiles.append(profile)

        return profiles