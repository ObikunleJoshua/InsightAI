class BusinessRules:
    """
    Scores how likely a column belongs
    to each business semantic.
    """

    @staticmethod
    def score(profile):

        scores = {
            "metrics": 0,
            "dimensions": 0,
            "entities": 0,
            "time_columns": 0,
            "identifiers": 0,
            "text_columns": 0,
        }

        # -----------------------
        # Time
        # -----------------------

        if profile["is_datetime"]:
            scores["time_columns"] += 100

        # -----------------------
        # Identifier
        # -----------------------

        if profile["unique_ratio"] > 0.95:
            scores["identifiers"] += 70

        name = profile["column"].lower()

        identifier_keywords = [
            "id",
            "code",
            "postal",
            "zip",
            "zipcode",
            "postal_code",
            "invoice",
            "order",
            "customer_id",
            "product_id",
        ]

        if any(keyword in name for keyword in identifier_keywords):
            scores["identifiers"] += 60

        # -----------------------
        # Metric
        # -----------------------

        if profile["is_numeric"]:
            scores["metrics"] += 50

            # Penalize numeric identifiers
            if any(keyword in name for keyword in identifier_keywords):
                scores["metrics"] -= 30

        if profile["statistics"] is not None:
            scores["metrics"] += 20

        # -----------------------
        # Dimension
        # -----------------------

        if (
            not profile["is_numeric"]
            and profile["unique_ratio"] < 0.30
        ):
            scores["dimensions"] += 70

        # -----------------------
        # Entity
        # -----------------------

        if (
            profile["is_text"]
            and 0.30 <= profile["unique_ratio"] <= 0.95
        ):
            scores["entities"] += 60

        # -----------------------
        # Text
        # -----------------------

        if (
            profile["average_length"]
            and profile["average_length"] > 40
        ):
            scores["text_columns"] += 80

        return scores