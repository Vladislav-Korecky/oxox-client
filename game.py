class Game:
    def __init__(self, y_size, x_size, players):
        self.board = []
        self.players = players

        for y in range(y_size):
            self.board.append([])

            for x in range(x_size):
                self.board[y].append(0)

    def play(self):
        while True:
            for player_index in range(len(self.players)):
                for line in self.board:
                    print(line)

                player_input = input()
                player_input = player_input.split(",")

                for i in range(len(player_input)):
                    player_input[i] = int(player_input[i])

                self.board[player_input[1]][player_input[0]] = self.players[player_index].player_num

                if self.is_win(player_input[0], player_input[1], player_index):
                    return player_index

    def is_win(self, x, y, player_index):
        for i in range(4):
            vector = []
            x2, y2 = x, y
            player_index2 = player_index

            if i == 0:
                vector = [1, 0]
            elif i == 1:
                vector = [0, 1]
            elif i == 2:
                vector = [1, 1]
            elif i == 3:
                vector = [-1, 1]

            while True:
                player_index2 += 1

                if player_index2 == len(self.players):
                    player_index2 = 0

                if y2 < 0 or y2 >= len(self.board):
                    break

                if x2 < 0 or x2 >= len(self.board[y2]):
                    break

                if self.board[y2][x2] != self.players[player_index2].player_num:
                    break

                x2 += vector[0]
                y2 += vector[1]

            for j in range(4):
                player_index2 += 1
                if player_index2 == len(self.players):
                    player_index2 = 0

                if y2 < 0 or y2 >= len(self.board):
                    break

                if x2 < 0 or x2 >= len(self.board[y2]):
                    break

                if self.board[y2][x2] != self.players[player_index2].player_num:
                    break

                if j == 3:
                    return True

                x2 -= vector[0]
                y2 -= vector[1]

        return False