"""
Experience Graph

Maintains:
- relational experience mapping
- recursive interaction graphs
- contextual linkage structures
- longitudinal knowledge associations
"""

from datetime import datetime

import networkx as nx

from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()


class ExperienceGraph:
    """
    Recursive relational experience graph system.
    """

    def __init__(self):

        logger.info(
            "Experience Graph initialized."
        )

        self.graph = nx.DiGraph()

    # --------------------------------------------------
    # Add Experience Node
    # --------------------------------------------------

    def add_experience(
        self,
        experience_id: str,
        label: str,
        metadata: dict = None
    ) -> dict:
        """
        Add experience node to graph.
        """

        logger.info(
            f"Adding experience node: {experience_id}"
        )

        self.graph.add_node(
            experience_id,
            label=label,
            metadata=metadata or {},
            timestamp=datetime.utcnow().isoformat()
        )

        return {
            "status": "node_added",
            "experience_id": experience_id
        }

    # --------------------------------------------------
    # Add Relationship Edge
    # --------------------------------------------------

    def add_relationship(
        self,
        source_id: str,
        target_id: str,
        relationship: str
    ) -> dict:
        """
        Add relationship edge between experiences.
        """

        logger.info(
            f"Linking {source_id} -> {target_id}"
        )

        self.graph.add_edge(
            source_id,
            target_id,
            relationship=relationship,
            timestamp=datetime.utcnow().isoformat()
        )

        return {
            "status": "relationship_added",
            "source": source_id,
            "target": target_id,
            "relationship": relationship
        }

    # --------------------------------------------------
    # Retrieve Connected Experiences
    # --------------------------------------------------

    def get_connections(
        self,
        experience_id: str
    ) -> dict:
        """
        Retrieve connected experience nodes.
        """

        logger.info(
            f"Retrieving connections for: "
            f"{experience_id}"
        )

        if experience_id not in self.graph:

            return {
                "status": "not_found",
                "experience_id": experience_id
            }

        successors = list(
            self.graph.successors(experience_id)
        )

        predecessors = list(
            self.graph.predecessors(experience_id)
        )

        return {
            "experience_id": experience_id,
            "connected_to": successors,
            "connected_from": predecessors
        }

    # --------------------------------------------------
    # Analyze Graph Stability
    # --------------------------------------------------

    def analyze_stability(self) -> dict:
        """
        Analyze relational graph stability.
        """

        logger.info(
            "Analyzing experience graph stability."
        )

        node_count = self.graph.number_of_nodes()

        edge_count = self.graph.number_of_edges()

        if node_count == 0:

            state = "initializing"

        elif edge_count < node_count:

            state = "sparse_relationships"

        elif edge_count >= node_count:

            state = "stable_relational_network"

        else:

            state = "undefined"

        logger.info(
            f"Experience graph state: {state}"
        )

        return {
            "state": state,
            "nodes": node_count,
            "edges": edge_count
        }

    # --------------------------------------------------
    # Graph Snapshot
    # --------------------------------------------------

    def snapshot(self) -> dict:
        """
        Generate experience graph snapshot.
        """

        logger.info(
            "Generating experience graph snapshot."
        )

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "node_count": self.graph.number_of_nodes(),
            "edge_count": self.graph.number_of_edges(),
            "stability": self.analyze_stability()
        }
