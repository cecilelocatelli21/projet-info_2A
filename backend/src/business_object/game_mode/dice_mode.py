import secrets
from datetime import datetime

from business_object.game import Game
from business_object.player import Player
from .game_mode import GameMode


class DiceMode(GameMode):

    def play(self, p1: Player, p2: Player) -> Game:
        d1 = secrets.choice(range(1, 7))
        d2 = secrets.choice(range(1, 7))

        if d1 > d2:
            winner = p1
        elif d2 > d1:
            winner = p2
        else:
            winner = None

        description = f"{p1.username} obtient {d1}, {p2.username} obtient {d2}"

        return Game(
            player1=p1,
            player2=p2,
            game_mode="dice",
            winner=winner,
            description=description,
            timestamp=datetime.now(),
        )