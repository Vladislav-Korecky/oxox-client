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
            for player in self.players:
                for line in self.board:
                    print(line)

                player_input = input()
                player_input = player_input.split(",")

                for i in range(len(player_input)):
                    player_input[i] = int(player_input[i])

                self.board[player_input[1]][player_input[0]] = player.player_num + 1
