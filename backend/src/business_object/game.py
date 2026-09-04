import datetime

from business_object.player import Player


class Game:
    "Documentation"

    def __init__(
        self,
        player1: Player,
        player2: Player,
        game_mode: str,
        winner: Player | None,
        description: str,
        timestamp: datetime
    ):
        """Constructor"""
        self.id_game = None
        self.player1 = player1
        self.player2 = player2
        self.game_mode = game_mode
        self.winner = winner
        self.description = description
        self.timestamp = timestamp

    def __str__(self):
        """Returns a string representation of the player.
        Returns:
            str: A string containing the two players.
        """
        winner_game = self.winner.username if self.winner else "Draw"
        return f"{self.game_mode} game between {self.player1.username} and {self.player2.username}. The winner is: {winner_game}"
