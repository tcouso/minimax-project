from game import Game

def print_board(board):
    for row in board:
        render_string = list(map(lambda x: " " if x == "" else x, row))
        print(render_string)



def minimax(state, game):
    """Computes the minimax value for a particular state."""
    state_copy = state


    if game.is_terminal(state_copy):
        # base case
        return game.utility(state_copy)

    elif not game.is_terminal(state_copy):
        if game.to_move(state_copy) == 'x':
            actions_minimax_values = []
            for action in game.actions(state_copy):
                # recursive step
                actions_minimax_values.append(
                    minimax(game.result(state_copy, action), game)
                )
            return max(actions_minimax_values)

        elif game.to_move(state_copy) == 'o':
            actions_minimax_values = []
            for action in game.actions(state_copy):
                # recursive step
                actions_minimax_values.append(
                    minimax(game.result(state_copy, action), game)
                )
            return min(actions_minimax_values)

if __name__ == "__main__":
    g = Game()
    test_position = [
        ["", "", ""], 
        ["x", "x", ""], 
        ["o", "o", ""]
        ]
    print(minimax(test_position, game=g))