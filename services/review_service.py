class ReviewService:
    """Analytics for customer review datasets."""

    @staticmethod
    def generate_review_kpis(df):

        kpis = {}

        # Number of reviews
        kpis["total_reviews"] = len(df)


        # Find rating column
        rating_column = None

        for column in df.columns:

            if "rating" in column.lower():
                rating_column = column
                break


        if rating_column:

            kpis["average_rating"] = round(
                df[rating_column].mean(),
                2
            )

            kpis["highest_rating"] = df[
                rating_column
            ].max()


        # Recommendation
        recommend_column = None

        for column in df.columns:

            if "recommend" in column.lower():
                recommend_column = column
                break


        if recommend_column:

            recommendation_rate = (
                df[recommend_column]
                .mean()
                * 100
            )

            kpis["recommendation_rate"] = round(
                recommendation_rate,
                2
            )


        # Department
        department_column = None

        for column in df.columns:

            if "department" in column.lower():
                department_column = column
                break


        if department_column:

            kpis["top_department"] = (
                df[department_column]
                .value_counts()
                .idxmax()
            )


        return kpis