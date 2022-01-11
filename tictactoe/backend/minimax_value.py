def minimax(state, game):
    """Computes the minimax value for a particular state."""
    if game.is_terminal(state):
        # base case
        return game.utility(state)

    elif not game.is_terminal(state):
        if game.to_move(state) == 'x':
            actions_minimax_values = []
            for action in game.actions(state):
                # recursive step
                actions_minimax_values.append(
                    minimax(game.result(state, action), game)
                )
            return max(actions_minimax_values)

        elif game.to_move(state) == 'o':
            actions_minimax_values = []
            for action in game.actions(state):
                # recursive step
                actions_minimax_values.append(
                    minimax(game.result(state, action), game)
                )
            return min(actions_minimax_values)