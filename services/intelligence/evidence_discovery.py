class EvidenceDiscovery:
    """
    Combines all discovered intelligence into
    a single business evidence package.
    """

    @staticmethod
    def discover(

        semantics,
        metrics,
        dimensions,
        relationships,
        patterns,

    ):

        evidence = {

            "business_summary": {},

            "key_metrics": {},

            "key_dimensions": {},

            "relationships": [],

            "patterns": {},

            "executive_highlights": [],
        }

        # -----------------------------
        # Metrics
        # -----------------------------

        evidence["key_metrics"] = metrics

        # -----------------------------
        # Dimensions
        # -----------------------------

        evidence["key_dimensions"] = dimensions

        # -----------------------------
        # Relationships
        # -----------------------------

        evidence["relationships"] = relationships.get(
            "relationships",
            [],
        )

        # -----------------------------
        # Patterns
        # -----------------------------

        evidence["patterns"] = patterns

        # -----------------------------
        # Executive Highlights
        # -----------------------------

        if dimensions["primary_dimensions"]:

            top = dimensions["primary_dimensions"][0]

            evidence["executive_highlights"].append(

                f"The strongest business dimension is '{top['column']}', "
                f"where '{top['top_value']}' leads with "
                f"{top['top_metric_value']}."

            )

        if relationships["relationships"]:

            rel = relationships["relationships"][0]

            evidence["executive_highlights"].append(

                f"The strongest relationship is between "
                f"{rel['metric_1']} and {rel['metric_2']} "
                f"({rel['correlation']})."

            )

        if patterns["dominant_groups"]:

            dom = patterns["dominant_groups"][0]

            evidence["executive_highlights"].append(

                f"{dom['winner']} contributes "
                f"{dom['share']}% of "
                f"{dom['metric']}."

            )

        evidence["business_summary"] = {

            "semantic_summary": semantics,

            "metric_count": len(
                metrics["primary_metrics"]
            ),

            "dimension_count": len(
                dimensions["primary_dimensions"]
            ),

            "relationship_count": len(
                relationships["relationships"]
            ),

            "pattern_count": len(
                patterns["dominant_groups"]
            ),
        }

        return evidence