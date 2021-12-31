class Game():
    def __init__(self) -> None:
        self.to_move = True
        self.turns = {
            True: 'x',
            False: 'o'
        }

    def utility(self, state, player):
        if (
            self.horizontal_win(state, player)
            or self.vertical_win(state, player)
            or self.diagonal1_win(state, player)
            or self.diagonal2_win(state, player)
        ):
            return 1

        elif self.full_grid(state, player):
            return 1/2

        else:
            return 0

    def is_terminal(self, state, player):
        """Terminal test."""
        if (
            self.horizontal_win(state, player)
            or self.vertical_win(state, player)
            or self.diagonal1_win(state, player)
            or self.diagonal2_win(state, player)
            or self.full_grid(state)
        ):
            return True
        else:
            return False

    def actions(self, state):
        """Returns the set of legal moves available from a grid state."""
        available_moves = set()
        for row_index, row in enumerate(state):
            for col_index, slot in enumerate(row):
                if slot == "":
                    available_moves.add((row_index, col_index))
        return available_moves

    def result(self, state, action):
        """
        Returns the resulting state from taking an action in a state.
        Action consists of making a move in a given coordinate
        """
        (row_index, col_index) = action
        state[row_index][col_index] = self.turns[self.to_move]
        return state

    # Terminal states

    def horizontal_win(self, state, player):
        for i in range(len(state)):
            if state[i][0] == state[i][1] == state[i][2] == player:
                return True
        return False

    def vertical_win(self, state, player):
        for i in range(len(state)):
            if state[0][i] == state[1][i] == state[2][i] == player:
                return True
        return False

    def diagonal1_win(self, state, player):
        "Northwest to southeast win."
        if state[0][0] == state[1][1] == state[2][2] == player:
            return True
        return False

    def diagonal2_win(self, state, player):
        "Southwest to northeast win."
        if state[2][0] == state[1][1] == state[0][2] == player:
            return True
        return False

    def full_grid(self, state):
        for row in state:
            for slot in row:
                if slot == "":
                    return False
        return True


if __name__ == "__main__":
    game = Game()
    test_position = [["o", "", "o"], ["", "x", "x"], ["x", "o", "x"]]
    print(game.result(test_position, (0, 1)))
