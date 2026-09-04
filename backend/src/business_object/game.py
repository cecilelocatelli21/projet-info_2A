import datetime

from business_object.player import Player


class Game:
    """ Classe modelisant un game
        Attributes:
        player1 (Player) : 
    """
    def __init__(
        self,
        player1 : Player,
        player2 : Player,
        game_mode : str,
        winner : Player | None,
        description: str,
        timestamp : datetime
    ):
        """Constructor"""
        self.player1 = player1
        self.player2 = player2
        self.game_mode = game_mode
        self.winner = winner
        self.description = description
        self.timestamp = timestamp
        self.id_game = None

    def __str__(self):
        winner_game = self.winner.username if self.winner else "Draw"
        return f"{self.game_mode} between {self.player1.username} and {self.player2.username}. \n Winner: {winner_game}"