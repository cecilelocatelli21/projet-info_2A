from fastapi import HTTPException

from dao.player_dao import PlayerDao
from business_object.game_mode.game_mode_factory import GameModeFactory
from business_object.scoring_strategy import ScoringStrategy
from utils.log_utils import log


class GameService:
    """Service that manages games."""

    @log
    def play(
        self,
        id_player: int,
        id_opponent: int,
        game_mode: str,
        **kwargs,
    ):
        """
        Executes a game between two players.

        Args:
            id_player (int): The unique identifier for the first player.
            id_opponent (int): The unique identifier for the opponent.
            game_mode (str): The game mode to play.
            **kwargs: Additional parameters required by the game mode.

        Returns:
            Game: The played game.

        Raises:
            HTTPException: 400 if the two players are the same.
            HTTPException: 404 if one or both players are not found.
        """

        # Vérifier que les joueurs sont différents
        if id_player == id_opponent:
            raise HTTPException(
                status_code=400,
                detail="Two different players required",
            )

        # Récupérer les joueurs
        p1 = PlayerDao().find_by_id(id_player)
        p2 = PlayerDao().find_by_id(id_opponent)

        if not p1 or not p2:
            raise HTTPException(
                status_code=404,
                detail="Player not found",
            )

        # Obtenir le mode de jeu grâce à la Factory
        mode = GameModeFactory.get_mode(game_mode)

        # Jouer la partie
        game = mode.play(p1, p2, **kwargs)

        # Mettre à jour les classements Elo
        ScoringStrategy.update_player_ratings(game)

        # Sauvegarder les nouveaux Elo
        PlayerDao().update(p1)
        PlayerDao().update(p2)

        # Retourner le Game
        return game