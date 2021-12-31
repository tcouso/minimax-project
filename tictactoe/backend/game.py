# Functions that formally define a game

# Terminal state functions

def horizontal_win(state):
    for i in range(len(state)):
        if state[i][0] == state[i][1] == state[i][2]:
            return True
    return False


def vertical_win(state):
    for i in range(len(state)):
        if state[0][i] == state[1][i] == state[2][i]:
            return True
    return False


def diagonal1_win(state):
    "Northwest to southeast win."
    if state[0][0] == state[1][1] == state[2][2]:
        return True
    return False


def diagonal2_win(state):
    "Southwest to northeast win."
    if state[2][0] == state[1][1] == state[0][2]:
        return True
    return False


def full_grid(state):
    for row in state:
        for slot in row:
            if slot == "":
                return 0
    return (True, '')


def is_terminal(state):
    """Terminal test."""
    if (
        horizontal_win(state)
        or vertical_win(state)
        or diagonal1_win(state)
        or diagonal2_win(state)
        or full_grid(state)
    ):
        return True
    else:
        return False


def to_move(state):
    """Asumes that max plays x's and always goes first"""
    x_count = 0
    o_count = 0
    for row in state:
        for token in row:
            if token == 'x':
                x_count += 1
            elif token == 'o':
                o_count += 1
    if x_count == o_count:
        return 'x'

    elif x_count > o_count:
        return 'o'


def utility(state, player='x'):
    if is_terminal(state):
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

    else:
        return 0


def actions(state):
    """Returns the set of legal moves available from a grid state."""
    available_moves = set()
    for row_index, row in enumerate(state):
        for col_index, slot in enumerate(row):
            if slot == "":
                available_moves.add((row_index, col_index))
    return available_moves


def result(state, action):
    """
    Returns the resulting state of taking an action fron a particular state.
    Action consists of making a move in a given coordinate
    """
    (row_index, col_index) = action
    state[row_index][col_index] = to_move(state)
    return state


if __name__ == "__main__":
    test_position = [["o", "x", "o"], ["x", "o", ""], ["x", "o", "x"]]
    print(result(test_position, (1, 2)))
