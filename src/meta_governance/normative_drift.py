"""
Normative Drift Engine

Detects:
- ethical drift
- recursive value instability
- principle divergence
- arbitration imbalance
- coexistence degradation
"""

from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()


class NormativeDrift:
    """
    Normative drift analysis engine.
    """

    def __init__(self):

        logger.info(
            "Normative Drift Engine initialized."
        )

        self.drift_threshold = 0.20

    # --------------------------------------------------
    # Evaluate Normative Drift
    # --------------------------------------------------

    def evaluate(
        self,
        previous_distribution: dict,
        current_distribution: dict
    ) -> dict:
        """
        Evaluate ethical principle drift.
        """

        logger.info(
            "Evaluating normative drift."
        )

        drift_results = []

        total_drift = 0.0

        # ----------------------------------------------
        # Compare Principle Weights
        # ----------------------------------------------

        for principle, previous_value in (
            previous_distribution.items()
        ):

            current_value = current_distribution.get(
                principle,
                previous_value
            )

            delta = abs(
                current_value - previous_value
            )

            total_drift += delta

            drift_results.append({
                "principle": principle,
                "previous": round(previous_value, 2),
                "current": round(current_value, 2),
                "drift_delta": round(delta, 2)
            })

        # ----------------------------------------------
        # Average Drift
        # ----------------------------------------------

        average_drift = (
            total_drift / len(previous_distribution)
        )

        average_drift = round(
            average_drift,
            2
        )

        # ----------------------------------------------
        # Drift Classification
        # ----------------------------------------------

        if average_drift <= 0.05:

            drift_state = "stable_alignment"

        elif average_drift <= 0.15:

            drift_state = "adaptive_variation"

        elif average_drift <= 0.30:

            drift_state = "elevated_normative_drift"

        else:

            drift_state = "critical_value_instability"

        logger.info(
            f"Normative drift evaluated: "
            f"{drift_state}"
        )

        return {
            "drift_state": drift_state,
            "average_drift": average_drift,
            "drift_results": drift_results
        }

    # --------------------------------------------------
    # Drift Risk Projection
    # --------------------------------------------------

    def project_risk(
        self,
        average_drift: float
    ) -> dict:
        """
        Project recursive normative instability risk.
        """

        logger.info(
            "Projecting normative drift risk."
        )

        if average_drift <= 0.05:

            projection = (
                "stable_recursive_alignment"
            )

        elif average_drift <= 0.15:

            projection = (
                "manageable_adaptive_variation"
            )

        elif average_drift <= 0.30:

            projection = (
                "recursive_alignment_risk"
            )

        else:

            projection = (
                "critical_recursive_divergence"
            )

        return {
            "risk_projection": projection,
            "average_drift": average_drift
        }

    # --------------------------------------------------
    # Principle Divergence Detection
    # --------------------------------------------------

    def detect_divergence(
        self,
        drift_results: list
    ) -> dict:
        """
        Detect principles with significant divergence.
        """

        logger.info(
            "Detecting principle divergence."
        )

        divergent_principles = []

        for result in drift_results:

            if result["drift_delta"] >= self.drift_threshold:

                divergent_principles.append(result)

        if divergent_principles:

            divergence_state = (
                "divergence_detected"
            )

        else:

            divergence_state = "stable"

        logger.info(
            f"Divergence detection complete: "
            f"{divergence_state}"
        )

        return {
            "divergence_state": divergence_state,
            "divergent_principles": divergent_principles,
            "count": len(divergent_principles)
        }
