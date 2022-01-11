from math import  inf

# Minimax search

def minimax_search(game, state):
    """Finds optimal move using minimax value"""
    player = game.to_move(state)
    value, move = max_value(game, state)
    return move


def max_value(game, state):
    if game.is_terminal(state):
        return (game.utility(state), None)
    value = -inf
    move = None
    for action in game.actions(state):
        value_2, action_2 = min_value(game, game.result(state, action))
        if value_2 > value:
            value, move = (value_2, action)
    return (value, move)


def min_value(game, state):
    if game.is_terminal(state):
        return (game.utility(state), None)
    value = inf
    move = None
    for action in game.actions(state):
        value_2, action_2 = max_value(game, game.result(state, action))
        if value_2 < value:
            value, move = (value_2, action)
    return (value, move)
