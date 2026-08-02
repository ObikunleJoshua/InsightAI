import pandas as pd


class RelationshipDiscovery:
    """
    Discovers relationships between business metrics.
    """

    @staticmethod
    def discover(df, metrics):

        result = {
            "relationships": []
        }

        primary_metrics = metrics.get(
            "primary_metrics",
            []
        )

        if len(primary_metrics) < 2:
            return result

        metric_columns = [
            metric["column"]
            for metric in primary_metrics
            if metric["column"] in df.columns
        ]

        correlation = df[
            metric_columns
        ].corr(numeric_only=True)

        visited = set()

        for metric1 in metric_columns:

            for metric2 in metric_columns:

                if metric1 == metric2:
                    continue

                pair = tuple(
                    sorted(
                        [metric1, metric2]
                    )
                )

                if pair in visited:
                    continue

                visited.add(pair)

                value = correlation.loc[
                    metric1,
                    metric2,
                ]

                if pd.isna(value):
                    continue

                result["relationships"].append({

                    "metric_1": metric1,

                    "metric_2": metric2,

                    "correlation": round(
                        value,
                        3,
                    ),

                    "strength":
                        RelationshipDiscovery._strength(
                            value
                        ),

                    "direction":
                        "Positive"
                        if value >= 0
                        else "Negative",
                })

        result["relationships"].sort(

            key=lambda x: abs(
                x["correlation"]
            ),

            reverse=True,
        )

        return result

    @staticmethod
    def _strength(value):

        value = abs(value)

        if value >= 0.80:
            return "Very Strong"

        if value >= 0.60:
            return "Strong"

        if value >= 0.40:
            return "Moderate"

        if value >= 0.20:
            return "Weak"

        return "Very Weak"