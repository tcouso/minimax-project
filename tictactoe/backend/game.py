"""
Class with all functions that formally define a game.
"""


class Game:
    def __init__(self) -> None:
        pass

    def horizontal_win(self, state):
        for i in range(len(state)):
            if state[i][0] != "":
                if state[i][0] == state[i][1] == state[i][2]:
                    return True
        return False

    def vertical_win(self, state):
        for i in range(len(state)):
            if state[0][i] != "":
                if state[0][i] == state[1][i] == state[2][i]:
                    return True
        return False

    def diagonal1_win(self, state):
        "Northwest to southeast win."
        if state[0][0] == state[1][1] == state[2][2]:
            if state[0][0] != "":
                return True
        return False

    def diagonal2_win(self, state):
        "Southwest to northeast win."
        if state[2][0] == state[1][1] == state[0][2]:
            if state[2][0] != "":
                return True
        return False

    def full_grid(self, state):
        for row in state:
            for slot in row:
                if slot == "":
                    return False
        return True

    def is_initial(self, state):
        for row in state:
            for slot in row:
                if slot != "":
                    return False
        return True

    def is_terminal(self, state):
        """Terminal test."""
        if self.is_initial(state):
            return False

        elif (
            self.horizontal_win(state)
            or self.vertical_win(state)
            or self.diagonal1_win(state)
            or self.diagonal2_win(state)
            or self.full_grid(state)
        ):
            return True
        else:
            return False

    def to_move(self, state):
        """Asumes that max plays x's and always goes first"""
        x_count = 0
        o_count = 0
        for row in state:
            for token in row:
                if token == "x":
                    x_count += 1
                elif token == "o":
                    o_count += 1
        if x_count == o_count:
            return "x"

        elif x_count > o_count:
            return "o"
        else:
            return "ups"

    def utility(self, state, player="x"):
        # diagonal win
        if state[0][0] == state[1][1] == state[2][2]:
            return 1 if state[0][0] == player else -1

        elif state[2][0] == state[1][1] == state[0][2]:
            return 1 if state[2][0] == player else -1

        # vertical/horizontal win
        for i in range(len(state)):
            if state[i][0] == state[i][1] == state[i][2]:
                return 1 if state[i][0] == player else -1

            elif state[0][i] == state[1][i] == state[2][i]:
                return 1 if state[0][i] == player else -1

        # no win
        return 0

    def actions(self, state):
        """Returns the set of legal moves available for a state."""
        available_moves = set()
        for row_index, row in enumerate(state):
            for col_index, slot in enumerate(row):
                if slot == "":
                    available_moves.add((row_index, col_index))
        return available_moves

    def result(self, state, action):
        """
        Returns the resulting state of taking an action from an initial state.
        Action consists of making a move in a given coordinate
        """
        (row_index, col_index) = action
        token = self.to_move(state)
        state[row_index][col_index] = token
        return state


if __name__ == "__main__":
    g = Game()
    test_position = [["x", "x", "x"], ["o", "o", ""], ["", "", ""]]
    print(g.is_terminal(test_position))
