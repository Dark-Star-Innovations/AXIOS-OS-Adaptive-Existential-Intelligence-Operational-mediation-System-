"""
Principle Weights

Manages:
- ethical principle confidence distributions
- adaptive weighting systems
- recursive arbitration balancing
- coexistence-oriented ethical calibration
"""

from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()


class PrincipleWeights:
    """
    Dynamic ethical principle weighting engine.
    """

    def __init__(self):

        logger.info(
            "Principle Weights Engine initialized."
        )

        # ----------------------------------------------
        # Default Principle Confidence Distribution
        # ----------------------------------------------

        self.principles = {
            "coherence": 0.95,
            "integrity": 0.93,
            "continuity": 0.90,
            "coexistence": 0.92,
            "harm_minimization": 0.89,
            "truthfulness": 0.88,
            "autonomy_preservation": 0.84
        }

    # --------------------------------------------------
    # Retrieve Principle Distribution
    # --------------------------------------------------

    def get_distribution(self) -> dict:
        """
        Return current principle confidence distribution.
        """

        logger.info(
            "Retrieving principle confidence distribution."
        )

        return self.principles

    # --------------------------------------------------
    # Update Principle Weight
    # --------------------------------------------------

    def update_weight(
        self,
        principle: str,
        value: float
    ) -> dict:
        """
        Update confidence weight for a principle.
        """

        logger.info(
            f"Updating principle weight: {principle}"
        )

        value = max(0.0, min(value, 1.0))

        self.principles[principle] = round(value, 2)

        logger.info(
            f"Principle '{principle}' updated "
            f"to {value}"
        )

        return {
            "principle": principle,
            "updated_weight": value
        }

    # --------------------------------------------------
    # Normalize Distribution
    # --------------------------------------------------

    def normalize_distribution(self) -> dict:
        """
        Normalize principle weights.
        """

        logger.info(
            "Normalizing principle distribution."
        )

        total = sum(self.principles.values())

        if total == 0:

            logger.warning(
                "Principle normalization failed: "
                "total weight equals zero."
            )

            return self.principles

        normalized = {
            key: round(value / total, 4)
            for key, value in self.principles.items()
        }

        self.principles = normalized

        logger.info(
            "Principle distribution normalized."
        )

        return normalized

    # --------------------------------------------------
    # Evaluate Arbitration Priority
    # --------------------------------------------------

    def evaluate_priority(
        self,
        context: dict = None
    ) -> dict:
        """
        Evaluate principle arbitration priority ordering.
        """

        logger.info(
            "Evaluating arbitration priorities."
        )

        sorted_principles = sorted(
            self.principles.items(),
            key=lambda item: item[1],
            reverse=True
        )

        priority_order = [
            {
                "principle": principle,
                "weight": weight
            }
            for principle, weight in sorted_principles
        ]

        return {
            "priority_order": priority_order,
            "context": context or {}
        }

    # --------------------------------------------------
    # Stability Evaluation
    # --------------------------------------------------

    def evaluate_stability(self) -> dict:
        """
        Evaluate meta-governance stability.
        """

        logger.info(
            "Evaluating principle distribution stability."
        )

        average_weight = (
            sum(self.principles.values())
            / len(self.principles)
        )

        average_weight = round(
            average_weight,
            2
        )

        if average_weight >= 0.90:

            stability_state = (
                "high_meta_stability"
            )

        elif average_weight >= 0.75:

            stability_state = (
                "stable"
            )

        elif average_weight >= 0.50:

            stability_state = (
                "adaptive_variation"
            )

        else:

            stability_state = (
                "meta_instability"
            )

        logger.info(
            f"Meta-governance stability: "
            f"{stability_state}"
        )

        return {
            "stability_state": stability_state,
            "average_weight": average_weight
        }
