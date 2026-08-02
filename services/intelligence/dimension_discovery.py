import pandas as pd


class DimensionDiscovery:
    """
    Discovers which business dimensions best explain
    the variation in important metrics.
    """

    @staticmethod
    def discover(df, semantics, metrics):

        result = {
            "primary_dimensions": [],
            "secondary_dimensions": [],
        }

        if not metrics["primary_metrics"]:
            return result

        primary_metric = metrics["primary_metrics"][0]["column"]

        for dimension in semantics["dimensions"]:

            column = dimension["column"]

            try:

                grouped = (
                    df.groupby(column)[primary_metric]
                    .sum()
                    .sort_values(ascending=False)
                )

                variation = grouped.std()

                score = DimensionDiscovery._score(
                    grouped,
                    variation,
                )

                item = {

                    "column": column,

                    "score": score,

                    "groups": len(grouped),

                    "top_value": grouped.index[0],

                    "top_metric_value": round(
                        grouped.iloc[0],
                        2,
                    ),
                }

                if score >= 80:

                    result["primary_dimensions"].append(
                        item
                    )

                else:

                    result["secondary_dimensions"].append(
                        item
                    )

            except Exception:

                continue

        result["primary_dimensions"].sort(

            key=lambda x: x["score"],

            reverse=True,
        )

        result["secondary_dimensions"].sort(

            key=lambda x: x["score"],

            reverse=True,
        )

        return result

    @staticmethod
    def _score(grouped, variation):

        score = 50

        if len(grouped) >= 3:
            score += 10

        if len(grouped) <= 30:
            score += 10

        if variation > 0:
            score += 20

        top_share = grouped.iloc[0] / grouped.sum()

        if top_share < 0.80:
            score += 10

        return min(score, 100)