import datetime
import secrets
import random

from business_object.game import Game
from business_object.game_mode.gamemode import GameMode
from business_object.player import Player


class FlipCoin(GameMode):
    "Documentation"

    def play(
        player1: Player,
        player2: Player
    ):

        result = secrets.choice(["heads", "tails"])
        choice = "heads"

        winner = player1 if result == choice else player2

        return Game(player1, player2, "Coinflip", winner, "Le jeu de pile ou face est terminé.", datetime.time)
