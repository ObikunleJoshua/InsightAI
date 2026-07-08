class DatasetClassifier:
    """Classifies uploaded datasets."""

    @staticmethod
    def classify(df):

        columns = [c.lower() for c in df.columns]

        business_columns = {
            "sales",
            "profit",
            "category",
            "region",
            "discount",
            "quantity",
        }

        review_columns = {
            "review text",
            "rating",
            "recommended ind",
            "department name",
            "class name",
        }

        business_matches = len(
            business_columns.intersection(columns)
        )

        review_matches = len(
            review_columns.intersection(columns)
        )

        if business_matches >= 3:
            return "Business Dataset"

        if review_matches >= 2:
            return "Customer Reviews Dataset"

        return "Generic Dataset"