from abc import ABC, abstractmethod

from business_object.game import Game
from business_object.player import Player


class GameMode(ABC):
    """
    Abstract base class representing a game mode.
    """

    @abstractmethod
    def play(self, p1: Player, p2: Player) -> Game:
        """
        Play a game between two players.

        Args:
            p1 (Player): First player.
            p2 (Player): Second player.

        Returns:
            Game: The result of the game.
        """
        pass
