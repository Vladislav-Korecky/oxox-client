from game import *
from player import *

# creating game
game = Game(6, 6, [Player(1), Player(2)])

# starting new match
winner = game.play()

# printing winner
print("Player number " + str(winner) + " won!")
