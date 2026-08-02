import pandas as pd


class PatternDiscovery:
    """
    Discovers high-level business patterns from the dataset.
    """

    @staticmethod
    def discover(df, metrics, dimensions):

        patterns = {
            "dominant_groups": [],
            "outliers": [],
            "concentration": [],
        }

        if not metrics["primary_metrics"]:
            return patterns

        metric = metrics["primary_metrics"][0]["column"]

        # -----------------------------------
        # Dominant Groups
        # -----------------------------------

        for dimension in dimensions["primary_dimensions"]:

            column = dimension["column"]

            try:

                grouped = (
                    df.groupby(column)[metric]
                    .sum()
                    .sort_values(ascending=False)
                )

                total = grouped.sum()

                top_value = grouped.index[0]

                top_metric = grouped.iloc[0]

                share = (
                    top_metric / total
                ) * 100

                patterns["dominant_groups"].append({

                    "dimension": column,

                    "winner": top_value,

                    "metric": metric,

                    "value": round(top_metric, 2),

                    "share": round(share, 2),
                })

            except Exception:
                continue

        # -----------------------------------
        # Numeric Outliers
        # -----------------------------------

        for metric_info in metrics["primary_metrics"]:

            column = metric_info["column"]

            try:

                q1 = df[column].quantile(0.25)
                q3 = df[column].quantile(0.75)

                iqr = q3 - q1

                lower = q1 - (1.5 * iqr)
                upper = q3 + (1.5 * iqr)

                count = len(
                    df[
                        (df[column] < lower)
                        |
                        (df[column] > upper)
                    ]
                )

                patterns["outliers"].append({

                    "metric": column,

                    "count": count,
                })

            except Exception:
                continue

        # -----------------------------------
        # Concentration
        # -----------------------------------

        for dimension in dimensions["primary_dimensions"]:

            column = dimension["column"]

            try:

                grouped = (
                    df.groupby(column)[metric]
                    .sum()
                    .sort_values(ascending=False)
                )

                cumulative = (
                    grouped.cumsum()
                    / grouped.sum()
                )

                top_needed = (
                    cumulative <= 0.80
                ).sum() + 1

                patterns["concentration"].append({

                    "dimension": column,

                    "groups_for_80_percent": int(top_needed),

                    "total_groups": len(grouped),
                })

            except Exception:
                continue

        return patterns