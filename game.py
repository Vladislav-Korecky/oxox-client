class Game:
    def __init__(self, y_size, x_size):
        self.board = []
        for y in range(y_size):
            self.board.append([])

            for x in range(x_size):
                self.board[y].append(0)