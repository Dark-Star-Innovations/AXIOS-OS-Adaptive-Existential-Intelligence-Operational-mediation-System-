"""
Episodic Memory

Stores:
- interaction episodes
- recursive reasoning events
- longitudinal operational experiences
- contextual continuity records
"""

from datetime import datetime

from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()


class EpisodicMemory:
    """
    Episodic interaction and experience memory system.
    """

    def __init__(self):

        logger.info(
            "Episodic Memory initialized."
        )

        self.episodes = []

    # --------------------------------------------------
    # Store Episode
    # --------------------------------------------------

    def store_episode(
        self,
        prompt: str,
        response: str,
        coherence_score: float,
        metadata: dict = None
    ) -> dict:
        """
        Store interaction episode.
        """

        logger.info(
            "Storing episodic memory entry."
        )

        episode = {
            "timestamp": datetime.utcnow().isoformat(),
            "prompt": prompt,
            "response": response,
            "coherence_score": round(
                coherence_score,
                2
            ),
            "metadata": metadata or {}
        }

        self.episodes.append(episode)

        logger.info(
            "Episode stored successfully."
        )

        return episode

    # --------------------------------------------------
    # Retrieve Recent Episodes
    # --------------------------------------------------

    def retrieve_recent(
        self,
        limit: int = 10
    ) -> list:
        """
        Retrieve recent episodic memories.
        """

        logger.info(
            f"Retrieving recent episodes "
            f"(limit={limit})."
        )

        return self.episodes[-limit:]

    # --------------------------------------------------
    # Search Episodes
    # --------------------------------------------------

    def search(
        self,
        keyword: str
    ) -> list:
        """
        Search episodic memory entries.
        """

        logger.info(
            f"Searching episodic memory: {keyword}"
        )

        keyword = keyword.lower()

        matches = []

        for episode in self.episodes:

            if (
                keyword in episode["prompt"].lower()
                or keyword in episode["response"].lower()
            ):

                matches.append(episode)

        logger.info(
            f"Memory search complete: "
            f"{len(matches)} match(es)."
        )

        return matches

    # --------------------------------------------------
    # Evaluate Episodic Stability
    # --------------------------------------------------

    def evaluate_stability(self) -> dict:
        """
        Evaluate episodic continuity stability.
        """

        logger.info(
            "Evaluating episodic memory stability."
        )

        if not self.episodes:

            return {
                "state": "initializing",
                "average_coherence": 1.0
            }

        coherence_scores = [
            episode["coherence_score"]
            for episode in self.episodes
        ]

        average_coherence = (
            sum(coherence_scores)
            / len(coherence_scores)
        )

        average_coherence = round(
            average_coherence,
            2
        )

        # ----------------------------------------------
        # Stability Classification
        # ----------------------------------------------

        if average_coherence >= 0.90:

            state = "high_stability"

        elif average_coherence >= 0.75:

            state = "stable"

        elif average_coherence >= 0.50:

            state = "adaptive_variation"

        else:

            state = "episodic_instability"

        logger.info(
            f"Episodic stability evaluated: {state}"
        )

        return {
            "state": state,
            "average_coherence": average_coherence,
            "episode_count": len(self.episodes)
        }

    # --------------------------------------------------
    # Memory Snapshot
    # --------------------------------------------------

    def snapshot(self) -> dict:
        """
        Generate episodic memory snapshot.
        """

        logger.info(
            "Generating episodic memory snapshot."
        )

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "episode_count": len(self.episodes),
            "stability": self.evaluate_stability()
        }
