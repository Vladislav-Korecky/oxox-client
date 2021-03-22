import unittest
from ..game import *
from ..player import *


class TestGame(unittest.TestCase):
    def setUp(self):
        self.gc = Game(6, 6, [Player(1), Player(2)])

    def test_reset_board(self):
        self.gc.reset_board()
        self.assertEqual(self.gc.board, [[0, 0, 0, 0, 0, 0]] * 6)

    def test_is_win(self):
        test = [
            {
                "board": [
                    [1, 2, 1, 2, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]
                ],
                "x": 3,
                "y": 0,
                "player_index": 1,
                "result": True
            },
            {
                "board": [
                    [2, 1, 2, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]
                ],
                "x": 3,
                "y": 0,
                "player_index": 0,
                "result": True
            },
            {
                "board": [
                    [0, 0, 2, 1, 2, 1],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]
                ],
                "x": 2,
                "y": 0,
                "player_index": 1,
                "result": True
            },
            {
                "board": [
                    [1, 2, 1, 2, 1, 0],
                    [2, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]
                ],
                "x": 3,
                "y": 0,
                "player_index": 1,
                "result": True
            },
            {
                "board": [
                    [1, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]
                ],
                "x": 0,
                "y": 3,
                "player_index": 1,
                "result": True
            },
            {
                "board": [
                    [1, 0, 0, 0, 0, 0],
                    [0, 2, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 2, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]
                ],
                "x": 3,
                "y": 3,
                "player_index": 1,
                "result": True
            },
            {
                "board": [
                    [1, 2, 1, 2, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]
                ],
                "x": 4,
                "y": 0,
                "player_index": 1,
                "result": False
            },
            {
                "board": [
                    [1, 2, 1, 2, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]
                ],
                "x": 3,
                "y": 0,
                "player_index": 0,
                "result": False
            }
        ]

        for board_data in test:
            self.gc.board = board_data["board"]
            self.assertEqual(self.gc.is_win(board_data["x"], board_data["y"], board_data["player_index"]), board_data["result"])
