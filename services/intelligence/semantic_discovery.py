from services.intelligence.column_profiler import ColumnProfiler
from services.intelligence.business_rules import BusinessRules


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

        scores = BusinessRules.score(profile)

        semantic = max(
            scores,
            key=scores.get,
        )

        return semantic

    @staticmethod
    def _confidence(profile, semantic):

        scores = BusinessRules.score(profile)

        total = sum(scores.values())

        if total == 0:
            return 0.0

        confidence = scores[semantic] / total

        return round(confidence, 2)