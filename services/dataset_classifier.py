class DatasetClassifier:
    """Detect the type of uploaded dataset."""

    @staticmethod
    def classify(metadata):

        columns = [
            column["name"].strip().lower()
            for column in metadata["columns_metadata"]
        ]

        business_keywords = [
            "sales",
            "profit",
            "region",
            "category",
            "discount",
            "quantity",
            "customer",
        ]

        review_keywords = [
            "review",
            "rating",
            "recommend",
            "department",
            "feedback",
            "title",
            "class",
        ]

        business_score = sum(
            any(keyword in column for column in columns)
            for keyword in business_keywords
        )

        review_score = sum(
            any(keyword in column for column in columns)
            for keyword in review_keywords
        )

        if business_score >= 3:

            confidence = round(
                business_score / len(business_keywords),
                2,
            )

            return {
                "type": "business",
                "label": "📈 Business Dataset",
                "confidence": confidence,
            }

        if review_score >= 3:

            confidence = round(
                review_score / len(review_keywords),
                2,
            )

            return {
                "type": "reviews",
                "label": "⭐ Customer Reviews Dataset",
                "confidence": confidence,
            }

        return {
            "type": "generic",
            "label": "📄 Generic Dataset",
            "confidence": 0.50,
        }