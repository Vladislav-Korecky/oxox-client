from game import *
from player import *

game = Game(6, 6, [Player(1), Player(2)])
winner = game.play()
print("Player number " + str(winner) + " won!")