import secrets
from datetime import datetime

from business_object.game import Game
from business_object.player import Player
from .game_mode import GameMode


class CoinFlipMode(GameMode):

    def play(self, p1: Player, p2: Player, choice: str) -> Game:
        # Tirage aléatoire : pile ou face
        result = secrets.choice(["pile", "face"])

        # Détermination du gagnant
        if choice == result:
            winner = p1
        else:
            winner = p2

        # Description de la partie
        description = (
            f"{p1.username} choisit {choice}. "
            f"Le résultat est {result}."
        )

        return Game(
            player1=p1,
            player2=p2,
            game_mode="coinflip",
            winner=winner,
            description=description,
            timestamp=datetime.now(),
        )