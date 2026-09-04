import os

from business_object.game import Game


class ScoringStrategy:
    """Strategy used to calculate and update player ratings."""

    @classmethod
    def calculate_expected_score(cls, elo_a, elo_b) -> float:
        """Calculates the probability of player A winning against player B."""
        return 1 / (1 + 10 ** ((elo_b - elo_a) / 400))

    @classmethod
    def calculate_new_ratings(
        cls, elo_a, elo_b, player_a_won: bool
    ) -> tuple[int, int]:
        """Computes the new Elo ratings for two players after a match."""
        k_factor = int(os.environ["ELO_K_FACTOR"])

        score_a = 1.0 if player_a_won else 0.0
        score_b = 1.0 - score_a

        new_elo_a = round(
            elo_a
            + k_factor
            * (score_a - cls.calculate_expected_score(elo_a, elo_b))
        )

        new_elo_b = round(
            elo_b
            + k_factor
            * (score_b - cls.calculate_expected_score(elo_b, elo_a))
        )

        return new_elo_a, new_elo_b

    @classmethod
    def update_player_ratings(cls, game: Game):
        """Calculates and updates the Elo attributes of the players.
        No update if there is no winner (draw).
        """
        if not game.winner:
            return

        p1 = game.player1
        p2 = game.player2
        winner = game.winner

        p1.elo, p2.elo = cls.calculate_new_ratings(
            p1.elo,
            p2.elo,
            player_a_won=(p1 == winner),
        )