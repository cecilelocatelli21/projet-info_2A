from datetime import datetime

from business_object.game import Game
from business_object.player import Player


p1 = Player(
    username="Jacky",
    elo=1200,
    email="jacky@test.fr"
)

p2 = Player(
    username="Jackie",
    elo=1200,
    email="jackie@test.fr"
)

g = Game(
    player1=p1,
    player2=p2,
    game_mode="coinflip",
    winner=p2,
    description="Jackie gagne la partie",
    timestamp=datetime.now()
)

print(g)

from business_object.game_mode.dice_mode import DiceMode

dice = DiceMode()
g = dice.play(p1, p2)

print(g)
print(g.description)

from business_object.game_mode.coin_flip_mode import CoinFlipMode

coin_flip = CoinFlipMode()

g = coin_flip.play(p1, p2, "pile")

print(g)
print(g.description)