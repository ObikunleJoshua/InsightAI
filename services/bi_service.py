import pandas as pd


class BusinessIntelligenceService:
    """Business KPI calculations."""

    @staticmethod
    def generate_kpis(df):

        kpis = {}

        # Total Sales
        if "sales" in df.columns.str.lower():

            sales_col = df.columns[
                df.columns.str.lower() == "sales"
            ][0]

            kpis["total_sales"] = round(
                df[sales_col].sum(), 2
            )

            kpis["average_order_value"] = round(
                df[sales_col].mean(), 2
            )

        # Total Profit
        if "profit" in df.columns.str.lower():

            profit_col = df.columns[
                df.columns.str.lower() == "profit"
            ][0]

            kpis["total_profit"] = round(
                df[profit_col].sum(), 2
            )

        # Orders
        kpis["total_orders"] = len(df)

        # Top Region
        if "region" in df.columns.str.lower():

            region_col = df.columns[
                df.columns.str.lower() == "region"
            ][0]

            sales_col = df.columns[
                df.columns.str.lower() == "sales"
            ][0]

            top_region = (
                df.groupby(region_col)[sales_col]
                .sum()
                .idxmax()
            )

            kpis["top_region"] = top_region

        # Top Category
        if "category" in df.columns.str.lower():

            category_col = df.columns[
                df.columns.str.lower() == "category"
            ][0]

            sales_col = df.columns[
                df.columns.str.lower() == "sales"
            ][0]

            top_category = (
                df.groupby(category_col)[sales_col]
                .sum()
                .idxmax()
            )

            kpis["top_category"] = top_category

        return kpis