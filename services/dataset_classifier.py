class DatasetClassifier:
    """Classifies uploaded datasets."""

    @staticmethod
    def classify(df):

        columns = [str(col).strip().lower() for col in df.columns]

        business_keywords = [
            "sales",
            "profit",
            "region",
            "category",
            "discount",
            "quantity",
        ]

        review_keywords = [
            "review",
            "rating",
            "recommend",
            "department",
            "class",
            "feedback",
            "title",
        ]

        business_score = sum(
            any(keyword in col for col in columns)
            for keyword in business_keywords
        )

        review_score = sum(
            any(keyword in col for col in columns)
            for keyword in review_keywords
        )

        if business_score >= 3:
            return "📈 Business Dataset"

        if review_score >= 3:
            return "⭐ Customer Reviews Dataset"

        return "📄 Generic Dataset"