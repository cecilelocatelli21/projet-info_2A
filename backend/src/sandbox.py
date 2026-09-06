import datetime

from business_object.game import Game
from business_object.game_mode.dicemode import DiceMode
from business_object.game_mode.coinflipmode import CoinFlipMode
from business_object.player import Player

p1 = Player("Toto", 1, "toto@caramail.com")
p2 = Player("Tata", 1, "toto@caramail.com")
#g = Game(p1, p2, "Coinflip", None, "Test", datetime.time())
#g = DiceMode.play(p1, p2)
g = CoinFlipMode.play(p1, p2)
print(g)
