from services.intelligence.semantic_discovery import SemanticDiscovery
from services.intelligence.metric_discovery import MetricDiscovery
from services.intelligence.dimension_discovery import DimensionDiscovery
from services.intelligence.relationship_discovery import RelationshipDiscovery
from services.intelligence.pattern_discovery import PatternDiscovery
from services.intelligence.evidence_discovery import EvidenceDiscovery


class IntelligenceEngine:
    """
    Executes the complete Intelligence Layer.
    """

    @staticmethod
    def analyze(df):

        # ---------------------------------
        # Semantic Discovery
        # ---------------------------------

        semantics = SemanticDiscovery.discover(df)

        # ---------------------------------
        # Metric Discovery
        # ---------------------------------

        metrics = MetricDiscovery.discover(
            None,
            semantics,
        )

        # ---------------------------------
        # Dimension Discovery
        # ---------------------------------

        dimensions = DimensionDiscovery.discover(
            df,
            semantics,
            metrics,
        )

        # ---------------------------------
        # Relationship Discovery
        # ---------------------------------

        relationships = RelationshipDiscovery.discover(
            df,
            metrics,
        )

        # ---------------------------------
        # Pattern Discovery
        # ---------------------------------

        patterns = PatternDiscovery.discover(
            df,
            metrics,
            dimensions,
        )

        # ---------------------------------
        # Evidence Discovery
        # ---------------------------------

        evidence = EvidenceDiscovery.discover(
            semantics,
            metrics,
            dimensions,
            relationships,
            patterns,
        )

        return {

            "semantics": semantics,

            "metrics": metrics,

            "dimensions": dimensions,

            "relationships": relationships,

            "patterns": patterns,

            "evidence": evidence,
        }