import datetime
import secrets
from random import randint

from business_object.game import Game
from business_object.game_mode.gamemode import GameMode
from business_object.player import Player


class CoinFlipMode(GameMode):
    """ classe modélisant un jeu de CoinFlip
    """

    def play(self, p1: Player, p2: Player, choice="heads"):
        result = secrets.choice(["heads", "tails"])
        winner = p1 if result == choice else p2
        return Game(p1, p2, "coinflip", winner, "No description", datetime.datetime.now())

