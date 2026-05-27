"""
Behavior Tracker

Tracks:
- behavioral continuity
- recursive interaction patterns
- longitudinal coherence
- adaptive identity evolution
"""

from datetime import datetime

from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()


class BehaviorTracker:
    """
    Behavioral continuity and interaction tracking system.
    """

    def __init__(self):

        logger.info("Behavior Tracker initialized.")

        # ----------------------------------------------
        # Behavioral History
        # ----------------------------------------------

        self.behavior_history = []

        self.current_behavioral_state = "stable"

    # --------------------------------------------------
    # Record Behavior Event
    # --------------------------------------------------

    def record_event(
        self,
        event_type: str,
        coherence_score: float,
        metadata: dict = None
    ) -> dict:
        """
        Record behavioral continuity event.
        """

        logger.info(
            f"Recording behavior event: {event_type}"
        )

        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": event_type,
            "coherence_score": round(coherence_score, 2),
            "metadata": metadata or {}
        }

        self.behavior_history.append(event)

        logger.info(
            "Behavior event recorded successfully."
        )

        return event

    # --------------------------------------------------
    # Evaluate Behavioral Continuity
    # --------------------------------------------------

    def evaluate_continuity(self) -> dict:
        """
        Evaluate longitudinal behavioral continuity.
        """

        logger.info(
            "Evaluating behavioral continuity."
        )

        if not self.behavior_history:

            return {
                "continuity_score": 1.0,
                "behavioral_state": "initializing"
            }

        coherence_scores = [
            event["coherence_score"]
            for event in self.behavior_history
        ]

        continuity_score = (
            sum(coherence_scores)
            / len(coherence_scores)
        )

        continuity_score = round(
            continuity_score,
            2
        )

        # ----------------------------------------------
        # Behavioral Stability Classification
        # ----------------------------------------------

        if continuity_score >= 0.90:

            self.current_behavioral_state = (
                "high_continuity"
            )

        elif continuity_score >= 0.75:

            self.current_behavioral_state = (
                "stable"
            )

        elif continuity_score >= 0.50:

            self.current_behavioral_state = (
                "adaptive_variation"
            )

        else:

            self.current_behavioral_state = (
                "behavioral_instability"
            )

        logger.info(
            f"Behavioral continuity score: "
            f"{continuity_score}"
        )

        return {
            "continuity_score": continuity_score,
            "behavioral_state": (
                self.current_behavioral_state
            ),
            "tracked_events": len(
                self.behavior_history
            )
        }

    # --------------------------------------------------
    # Retrieve Behavioral Timeline
    # --------------------------------------------------

    def get_behavioral_timeline(self) -> list:
        """
        Return complete behavioral event timeline.
        """

        logger.info(
            "Retrieving behavioral timeline."
        )

        return self.behavior_history

    # --------------------------------------------------
    # Recursive Pattern Analysis
    # --------------------------------------------------

    def analyze_patterns(self) -> dict:
        """
        Analyze recursive behavioral patterns.
        """

        logger.info(
            "Analyzing recursive behavioral patterns."
        )

        event_count = len(self.behavior_history)

        if event_count == 0:

            return {
                "pattern_state": "no_data",
                "event_count": 0
            }

        average_coherence = (
            sum(
                event["coherence_score"]
                for event in self.behavior_history
            )
            / event_count
        )

        average_coherence = round(
            average_coherence,
            2
        )

        if average_coherence >= 0.90:

            pattern_state = (
                "stable_recursive_patterns"
            )

        elif average_coherence >= 0.75:

            pattern_state = (
                "adaptive_recursive_patterns"
            )

        else:

            pattern_state = (
                "unstable_recursive_patterns"
            )

        logger.info(
            f"Pattern analysis complete: "
            f"{pattern_state}"
        )

        return {
            "pattern_state": pattern_state,
            "average_coherence": average_coherence,
            "event_count": event_count
        }
