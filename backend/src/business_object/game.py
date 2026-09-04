from datetime import datetime

from .player import Player


class Game:
    """
    Class representing a Game.
    """

    def __init__(
        self,
        player1,
        player2,
        game_mode,
        winner,
        description,
        timestamp,
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
        """Returns a string representation of the game."""
        if self.winner is None:
            winner = "Égalité"
        else:
            winner = self.winner.username

        if self.game_mode == "coinflip":
            mode = "Pile ou face"
        elif self.game_mode == "dice":
            mode = "Dés"
        else:
            mode = self.game_mode

        return f"{mode} entre {self.player1.username} et {self.player2.username}. Gagnante : {winner}"