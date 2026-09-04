from business_object.game_mode.coinflipmode import CoinFlipMode
from business_object.game_mode.dicemode import DiceMode
from business_object.game_mode.gamemode import GameMode


class GameModeFactory:
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

        # Code here
        if game_mode not in ["coinflip", "dice"]:
            raise ValueError("game_mode must be 'coinflip' or 'dice'")
        if game_mode == "coinflip":
            return CoinFlipMode()
        else:
            return DiceMode()
