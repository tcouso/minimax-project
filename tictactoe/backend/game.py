"""
Class with all functions that formally define a game.
"""


class Game:
    def __init__(self) -> None:
        pass

    def horizontal_win(self, state):
        for i in range(len(state)):
            token = state[i][0]
            if state[i][0] == state[i][1] == state[i][2] and token != "":
                return True, token
        return False, token

    def vertical_win(self, state):
        for i in range(len(state)):
            token = state[0][i]
            if state[0][i] == state[1][i] == state[2][i] and token != "":
                return True, token
        return False, token

    def diagonal1_win(self, state):
        "Northwest to southeast win."
        token = state[0][0]
        if state[0][0] == state[1][1] == state[2][2] and token != "":
            return True, token
        return False, token

    def diagonal2_win(self, state):
        "Southwest to northeast win."
        token = state[2][0]
        if state[2][0] == state[1][1] == state[0][2] and token != "":
            return True, token
        return False, token

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
        diag1, _= self.diagonal1_win(state)
        diag2, _= self.diagonal2_win(state)
        hwin, _ = self.horizontal_win(state)
        vwin, _ = self.vertical_win(state)
        full = self.full_grid(state)

        if self.is_initial(state):
            return False

        elif (
            hwin
            or vwin
            or diag1
            or diag2
            or full
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

    def utility(self, state, player="x"):
        diag1, token_diag1 = self.diagonal1_win(state)
        diag2, token_diag2 = self.diagonal2_win(state)
        hwin, token_hwin = self.horizontal_win(state)
        vwin, token_vwin = self.vertical_win(state)
        if diag1:
            return 1 if token_diag1 == player else -1

        elif diag2:
            return 1 if token_diag2 == player else -1

        elif hwin:
            return 1 if token_hwin == player else -1
        
        elif vwin:
            return 1 if token_vwin == player else -1

        else:
            return 0  # no win

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
    test_position = [
        ["", "", "o"], 
        ["", "o", ""], 
        ["o", "", ""]
        ]
    print(g.utility(test_position))
