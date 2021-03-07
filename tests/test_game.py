import unittest
from ..game import *
from ..player import *


class TestGame(unittest.TestCase):
    def setUp(self):
        self.gc = Game(6, 6, [Player(1), Player(2)])

    def test_reset_board(self):
        self.gc.reset_board()
        self.assertEqual(self.gc.board, [[0, 0, 0, 0, 0, 0]] * 6)
