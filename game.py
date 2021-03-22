class Game:
    def __init__(self, x_size, y_size, players):
        # init
        self.board = []
        self.players = players
        self.x_size = x_size
        self.y_size = y_size

        # creating board
        self.reset_board()

    def reset_board(self):
        self.board = []
        
        for y in range(self.y_size):
            self.board.append([])

            for x in range(self.x_size):
                self.board[y].append(0)

    def play(self):
        player_index = 0

        # game loop
        while True:
            # printing board state
            self.print_board()

            # getting tile position from player
            player_input = self.get_input()

            # updating board
            if self.board[player_input[1]][player_input[0]] == 0:
                self.board[player_input[1]][player_input[0]] = self.players[player_index].player_num
            else:
                continue

            # checking for win
            if self.is_win(player_input[0], player_input[1], player_index):
                return player_index

            # giving turn to another player
            player_index += 1

            if player_index == len(self.players):
                player_index = 0

    def is_win(self, x, y, player_index):
        # checking four directions (vectors)
        for i in range(4):
            # init
            vector = []
            x2, y2 = x, y
            player_index2 = player_index

            # selecting vector
            if i == 0:
                vector = [1, 0]
            elif i == 1:
                vector = [0, 1]
            elif i == 2:
                vector = [1, 1]
            elif i == 3:
                vector = [-1, 1]

            # checking tiles
            while True:
                # checking if tile exists
                if not self.tile_exists(x2, y2):
                    break

                # checking if tile belongs to player
                if self.board[y2][x2] != self.players[player_index2].player_num:
                    break

                # changing tile
                x2 += vector[0]
                y2 += vector[1]

                # changing player
                player_index2 += 1

                if player_index2 == len(self.players):
                    player_index2 = 0

            # checking direction in reverse for signs of winning combination
            for j in range(4):
                # changing player
                player_index2 += 1

                if player_index2 == len(self.players):
                    player_index2 = 0

                # changing tile
                x2 -= vector[0]
                y2 -= vector[1]

                # checking if tile exists
                if not self.tile_exists(x2, y2):
                    break

                # checking if tile belongs to player
                if self.board[y2][x2] != self.players[player_index2].player_num:
                    break

                # checking for end of pattern
                if j == 3:
                    return True

        return False

    def print_board(self):
        for line in self.board:
            print(line)

    def get_input(self):
        player_input = input().split(",")

        processed_input = []
        for i in range(len(player_input)):
            processed_input.append(int(player_input[i]))

        return processed_input

    def tile_exists(self, x, y):
        # checking y axis
        if y < 0 or y >= len(self.board):
            return False

        # checking x axis
        if x < 0 or x >= len(self.board[y]):
            return False

        return True
