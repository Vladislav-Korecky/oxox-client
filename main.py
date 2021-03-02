from game import *
from player import *

game = Game(6, 6, [Player(0), Player(1)])
for y in game.board:
    print(y)
game.play()