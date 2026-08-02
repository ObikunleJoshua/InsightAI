from services.intelligence.column_profiler import ColumnProfiler


class SemanticDiscovery:
    """
    Discovers the business semantics of dataset columns.

    It DOES NOT inspect the dataframe directly.

    It only reasons from the Column Profiles.
    """

    @staticmethod
    def discover(df):

        profiles = ColumnProfiler.profile(df)

        semantics = {

            "metrics": [],

            "dimensions": [],

            "entities": [],

            "time_columns": [],

            "identifiers": [],

            "text_columns": [],

            "unknown_columns": [],
        }

        for profile in profiles:

            semantic = SemanticDiscovery._classify(profile)

            semantics[semantic].append({

                "column": profile["column"],

                "confidence": SemanticDiscovery._confidence(
                    profile,
                    semantic,
                ),

                "profile": profile,
            })

        return semantics

    @staticmethod
    def _classify(profile):

        # -----------------------
        # Time
        # -----------------------

        if profile["is_datetime"]:

            return "time_columns"

        # -----------------------
        # Metric
        # -----------------------

        if profile["is_numeric"]:

            return "metrics"

        # -----------------------
        # Identifier
        # -----------------------

        if profile["unique_ratio"] >= 0.95:

            return "identifiers"

        # -----------------------
        # Dimension
        # -----------------------

        if profile["unique_ratio"] <= 0.30:

            return "dimensions"

        # -----------------------
        # Text
        # -----------------------

        if (

            profile["is_text"]

            and profile["average_length"] is not None

            and profile["average_length"] > 40

        ):

            return "text_columns"

        # -----------------------
        # Entity
        # -----------------------

        if (

            profile["is_text"]

            and profile["unique_ratio"] > 0.30

        ):

            return "entities"

        # -----------------------
        # Unknown
        # -----------------------

        return "unknown_columns"

    @staticmethod
    def _confidence(profile, semantic):

        score = 0.50

        if semantic == "metrics":

            if profile["is_numeric"]:

                score += 0.40

            if profile["statistics"]:

                score += 0.10

        elif semantic == "time_columns":

            if profile["is_datetime"]:

                score += 0.50

        elif semantic == "identifiers":

            score += min(
                profile["unique_ratio"],
                0.50,
            )

        elif semantic == "dimensions":

            score += 0.40 * (
                1 - profile["unique_ratio"]
            )

        elif semantic == "entities":

            score += 0.30

        elif semantic == "text_columns":

            score += 0.30

        return round(

            min(score, 1.0),

            2,
        )