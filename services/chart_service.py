import plotly.express as px


class ChartService:

    @staticmethod
    def sales_by_region(df):

        if (
            "Region" not in df.columns
            or
            "Sales" not in df.columns
        ):
            return None

        chart_data = (
            df.groupby("Region")["Sales"]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            chart_data,
            x="Region",
            y="Sales",
            title="Sales by Region"
        )

        return fig

    @staticmethod
    def sales_by_category(df):

        if (
            "Category" not in df.columns
            or
            "Sales" not in df.columns
        ):
            return None

        chart_data = (
            df.groupby("Category")["Sales"]
            .sum()
            .reset_index()
        )

        fig = px.pie(
            chart_data,
            names="Category",
            values="Sales",
            title="Sales by Category"
        )

        return fig

    @staticmethod
    def ratings_distribution(df):

        rating_column = None

        for column in df.columns:

            if "rating" in column.lower():
                rating_column = column
                break

        if rating_column is None:
            return None

        fig = px.histogram(
            df,
            x=rating_column,
            title="Rating Distribution"
        )

        return fig