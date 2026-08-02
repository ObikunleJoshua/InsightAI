class MetricDiscovery:
    """
    Discovers the importance of business metrics.

    Input:
        - Column Profiles
        - Semantic Discovery

    Output:
        {
            "primary_metrics": [],
            "secondary_metrics": [],
            "derived_metrics": []
        }
    """

    @staticmethod
    def discover(profiles=None, semantics=None):

        result = {

            "primary_metrics": [],

            "secondary_metrics": [],

            "derived_metrics": [],
        }

        metrics = semantics.get(
            "metrics",
            [],
        )

        for metric in metrics:

            profile = metric["profile"]

            score = MetricDiscovery._score(profile)

            item = {

                "column": profile["column"],

                "score": score,

                "statistics": profile["statistics"],
            }

            if score >= 80:

                result["primary_metrics"].append(item)

            else:

                result["secondary_metrics"].append(item)

        result["primary_metrics"].sort(

            key=lambda x: x["score"],

            reverse=True,
        )

        result["secondary_metrics"].sort(

            key=lambda x: x["score"],

            reverse=True,
        )

        result["derived_metrics"] = MetricDiscovery._derived_metrics(
            metrics
        )

        return result

    @staticmethod
    def _score(profile):

        score = 0

        if profile["is_numeric"]:

            score += 40

        if profile["statistics"]:

            score += 20

        if profile["unique_ratio"] > 0.50:

            score += 20

        if profile["null_ratio"] < 0.10:

            score += 20

        return score

    @staticmethod
    def _derived_metrics(metrics):

        names = [

            metric["column"].lower()

            for metric in metrics
        ]

        derived = []

        if (

            "sales" in names

            and "profit" in names

        ):

            derived.append(

                "Profit Margin"

            )

        if (

            "revenue" in names

            and "cost" in names

        ):

            derived.append(

                "Gross Margin"

            )

        return derived