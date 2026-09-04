import datetime
from random import randint

from business_object.game import Game
from business_object.game_mode.gamemode import GameMode
from business_object.player import Player


class DiceMode(GameMode):
    """ classe modelisant le jeu de dés
    """
    def play(self, p1: Player, p2: Player):
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        if d1 > d2:
            winner = p1
        elif d2 > d1:
            winner = p2
        else:
            winner = None
        return Game(p1, p2, "dice", winner, "No description", datetime.datetime.now())
