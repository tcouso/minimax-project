class UsedSlotError(Exception):
    def __init__(self, coordinates, token):
        super().__init__(f"Slot in {coordinates} is already filled with {token} token")


class Board:
    def __init__(self):
        self.__game_state = False
        self.__game_winner = None
        self.__grid = [[None, None, None], [None, None, None], [None, None, None]]
        self.__move_translator = {
            "a1": [0, 0],
            "a2": [0, 1],
            "a3": [0, 2],
            "b1": [1, 0],
            "b2": [1, 1],
            "b3": [1, 2],
            "c1": [2, 0],
            "c2": [2, 1],
            "c3": [2, 2],
        }

    @property
    def game_state(self):
        return self.__game_state

    @game_state.setter
    def game_state(self, new_state):
        self.__game_state = new_state

    @property
    def game_winner(self):
        return self.__game_winner

    @game_winner.setter
    def game_winner(self, winner):
        self.__game_winner = winner

    def render_board(self):
        print("TicTacToe!\n")
        for row in self.__grid:
            print(f"{row[0]} {row[1]} {row[2]}\n")

    def game_move(self, player, move):
        try:
            if player:
                token = "O"
            else:
                token = "X"
            list_coordinates = self.__move_translator[move]
            self.place_token(token, list_coordinates)
        except (KeyError, UsedSlotError):
            print("Invalid coordinate")

    def place_token(self, token, coordinates):
        try:
            x, y = coordinates
            slot = self.__grid[y][x]
            if slot is not None:
                raise UsedSlotError(coordinates, token)
            else:
                self.__grid[y][x] = token
        except UsedSlotError as err:
            raise err

    def check_winner(self):
        for token in ["O", "X"]:
            if (
                self.win_1(token)
                or self.win_2(token)
                or self.win_3(token)
                or self.win_4(token)
            ):
                self.game_state = True
                self.game_winner = self.__player_translator[token]

    def win_1(self, token):
        "Horizontal win."
        for i in range(len(self.__grid)):
            if self.__grid[i][0] == self.__grid[i][1] == self.__grid[i][2] == token:
                return True
        return False

    def win_2(self, token):
        "Vertical win."
        for i in range(len(self.__grid)):
            if self.__grid[0][i] == self.__grid[1][i] == self.__grid[2][i] == token:
                return True
        return False

    def win_3(self, token):
        "Northwest to southeast win."
        if self.__grid[0][0] == self.__grid[1][1] == self.__grid[2][2] == token:
            return True
        return False

    def win_4(self, token):
        "Southwest to northeast win."
        if self.__grid[2][0] == self.__grid[1][1] == self.__grid[0][2] == token:
            return True
        return False


def start_game(moves):
    board = Board()
    player = True
    for move in moves:

        # while True:
        #     board.render_board()
        #     board.game_move(player, move)
        #     if board.game_state:
        #         break
        #     player = not player
        board.game_move(player, move)
        board.render_board()


if __name__ == "__main__":
    moves = ["a2", "b3", "b3"]
    start_game(moves)
