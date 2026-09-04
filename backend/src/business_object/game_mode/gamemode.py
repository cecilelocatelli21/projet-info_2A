from abc import ABC, abstractmethod

from business_object.player import Player


class GameMode(ABC):
    """classe abstraite représentant un mode de jeu
    """
    @abstractmethod
    def play(p1: Player, p2: Player):
        pass

