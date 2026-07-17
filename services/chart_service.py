import plotly.express as px


class ChartService:

    @staticmethod
    def _find_column(df, keywords):
        """
        Finds the first column containing any of the supplied keywords.
        """
        for column in df.columns:
            column_lower = column.lower()
            if any(keyword in column_lower for keyword in keywords):
                return column
        return None

    @staticmethod
    def sales_by_region(df):

        region_column = ChartService._find_column(
            df,
            ["region"]
        )

        sales_column = ChartService._find_column(
            df,
            ["sales", "revenue"]
        )

        if region_column is None or sales_column is None:
            return None

        chart_data = (
            df.groupby(region_column)[sales_column]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            chart_data,
            x=region_column,
            y=sales_column,
            title="Sales by Region"
        )

        return fig

    @staticmethod
    def sales_by_category(df):

        category_column = ChartService._find_column(
            df,
            ["category"]
        )

        sales_column = ChartService._find_column(
            df,
            ["sales", "revenue"]
        )

        if category_column is None or sales_column is None:
            return None

        chart_data = (
            df.groupby(category_column)[sales_column]
            .sum()
            .reset_index()
        )

        fig = px.pie(
            chart_data,
            names=category_column,
            values=sales_column,
            title="Sales by Category"
        )

        return fig

    @staticmethod
    def ratings_distribution(df):

        rating_column = ChartService._find_column(
            df,
            ["rating"]
        )

        if rating_column is None:
            return None

        fig = px.histogram(
            df,
            x=rating_column,
            title="Rating Distribution"
        )

        return fig