import pandas as pd


class EvidenceBuilder:
    """
    Builds structured business evidence from a dataset.

    This evidence is supplied to the AI Business Analyst
    before any AI reasoning takes place.
    """

    @staticmethod
    def build(df: pd.DataFrame) -> dict:

        evidence = {}

        evidence["rows"] = len(df)
        evidence["columns"] = len(df.columns)

        # ----------------------------
        # Revenue
        # ----------------------------
        if "Sales" in df.columns:

            evidence["total_sales"] = round(
                df["Sales"].sum(),
                2,
            )

            evidence["average_sales"] = round(
                df["Sales"].mean(),
                2,
            )

        # ----------------------------
        # Profit
        # ----------------------------
        if "Profit" in df.columns:

            evidence["total_profit"] = round(
                df["Profit"].sum(),
                2,
            )

            evidence["average_profit"] = round(
                df["Profit"].mean(),
                2,
            )

        # ----------------------------
        # Orders
        # ----------------------------
        evidence["total_records"] = len(df)

        # ----------------------------
        # Average Order Value
        # ----------------------------
        if (
            "Sales" in df.columns
            and len(df) > 0
        ):

            evidence["average_order_value"] = round(
                df["Sales"].sum() / len(df),
                2,
            )

        # ----------------------------
        # Top Region
        # ----------------------------
        if (
            "Region" in df.columns
            and "Sales" in df.columns
        ):

            region_sales = (
                df.groupby("Region")["Sales"]
                .sum()
                .sort_values(ascending=False)
            )

            evidence["top_region"] = (
                region_sales.index[0]
            )

        # ----------------------------
        # Top Category
        # ----------------------------
        if (
            "Category" in df.columns
            and "Sales" in df.columns
        ):

            category_sales = (
                df.groupby("Category")["Sales"]
                .sum()
                .sort_values(ascending=False)
            )

            evidence["top_category"] = (
                category_sales.index[0]
            )

        # ----------------------------
        # Top Customer Segment
        # ----------------------------
        if (
            "Segment" in df.columns
            and "Sales" in df.columns
        ):

            segment_sales = (
                df.groupby("Segment")["Sales"]
                .sum()
                .sort_values(ascending=False)
            )

            evidence["top_segment"] = (
                segment_sales.index[0]
            )

        return evidence