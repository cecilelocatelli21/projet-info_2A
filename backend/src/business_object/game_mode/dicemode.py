import datetime
import random

from business_object.game import Game
from business_object.game_mode.gamemode import GameMode
from business_object.player import Player


class Dice(GameMode):
    "Documentation"

    def play(
        player1: Player,
        player2: Player
    ):

        result_player1 = random.randint(1, 6)
        result_player2 = random.randint(1, 6)

        if result_player1 > result_player2:
            winner = player1
        elif result_player1 < result_player2:
            winner = player2
        else:
            winner = None

        return Game(player1, player2, "Dice", winner, "Le jeu de dé est terminé.", datetime.time)
