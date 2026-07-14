import pandas as pd

from pandas.api.types import (
    is_object_dtype,
    is_categorical_dtype,
    is_bool_dtype,
)


class FilterService:
    """
    Handles dynamic dashboard filtering.
    """

    @staticmethod
    def get_filter_columns(df: pd.DataFrame) -> list:
        """
        Return columns suitable for dashboard filtering.
        """

        columns = []

        for column in df.columns:

            series = df[column]

            # Ignore columns with only one value
            if series.nunique(dropna=True) <= 1:
                continue

            # Text, category and boolean columns
            if (
                is_object_dtype(series)
                or is_categorical_dtype(series)
                or is_bool_dtype(series)
            ):

                if series.nunique(dropna=True) <= 50:
                    columns.append(column)

        return columns

    @staticmethod
    def apply_filters(
        df: pd.DataFrame,
        filters: dict,
    ) -> pd.DataFrame:
        """
        Apply all selected filters to the dataset.
        """

        filtered_df = df.copy()

        for column, value in filters.items():

            if value != "All":

                filtered_df = filtered_df[
                    filtered_df[column] == value
                ]

        return filtered_df