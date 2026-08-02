class EvidenceFormatter:
    """
    Converts structured intelligence into an
    executive-readable briefing for the LLM.
    """

    @staticmethod
    def format(evidence):

        lines = []

        # --------------------------------
        # Executive Highlights
        # --------------------------------

        lines.append("EXECUTIVE HIGHLIGHTS")

        for item in evidence.get(
            "executive_highlights",
            [],
        ):

            lines.append(f"- {item}")

        lines.append("")

        # --------------------------------
        # Key Metrics
        # --------------------------------

        lines.append("KEY METRICS")

        metrics = evidence.get(
            "key_metrics",
            {},
        )

        for metric in metrics.get(
            "primary_metrics",
            [],
        ):

            lines.append(

                f"- {metric['column']} (Score: {metric['score']})"

            )

        lines.append("")

        # --------------------------------
        # Key Dimensions
        # --------------------------------

        lines.append("KEY DIMENSIONS")

        dimensions = evidence.get(
            "key_dimensions",
            {},
        )

        for dimension in dimensions.get(
            "primary_dimensions",
            [],
        ):

            lines.append(

                f"- {dimension['column']} | "
                f"Top: {dimension['top_value']} | "
                f"Value: {dimension['top_metric_value']}"

            )

        lines.append("")

        # --------------------------------
        # Relationships
        # --------------------------------

        lines.append("KEY RELATIONSHIPS")

        for relation in evidence.get(
            "relationships",
            [],
        )[:5]:

            lines.append(

                f"- {relation['metric_1']} ↔ "
                f"{relation['metric_2']} | "
                f"{relation['direction']} | "
                f"{relation['strength']} | "
                f"{relation['correlation']}"

            )

        lines.append("")

        # --------------------------------
        # Patterns
        # --------------------------------

        lines.append("DISCOVERED PATTERNS")

        patterns = evidence.get(
            "patterns",
            {},
        )

        for pattern in patterns.get(
            "dominant_groups",
            [],
        ):

            lines.append(

                f"- {pattern['winner']} contributes "
                f"{pattern['share']}% of "
                f"{pattern['metric']}"

            )

        return "\n".join(lines)