from business_object.game import Game
from business_object.game_mode.dicemode import DiceMode
from business_object.game_mode.coinflipmode import CoinFlipMode
from business_object.player import Player
from business_object.game_mode.gamemodefactory import GameModeFactory

p1 = Player("toto", 1000, "toto@a.fr")
p2 = Player("cece", 1100, "cece@a.fr")
for i in range(10):
    g = CoinFlipMode().play(p1, p2)
    print(g)

gmf = GameModeFactory.get_mode("coinflip")
print(gmf)
