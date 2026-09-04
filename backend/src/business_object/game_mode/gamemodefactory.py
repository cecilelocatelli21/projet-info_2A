import datetime
import secrets
import random

from business_object.game import Game
from business_object.game_mode.dicemode import Dice
from business_object.game_mode.flipcoin import FlipCoin
from business_object.game_mode.gamemode import GameMode
from business_object.player import Player


class GameModeFactory:
    "Documentation"

    @classmethod
    def get_mode(cls, game_mode: str) -> GameMode:
        """
        Returns the corresponding GameMode object.
        Args:
            game_mode (str): The identifier of the game mode (e.g., 'coinflip', 'dice').
        Returns:
            GameMode: An instance of a class implementing GameMode.
        Raises:
            ValueError: If the requested game_mode is not supported.
        """
        if game_mode == 'dice'
            return DiceMode()
        if game_mode == 'flipcoin'
            return FlipCoinMode()
        if game_mode not in ("flipcoin", "dice")
            raise ValueError "gamemode must be 'coinflip' or 'dice'"
