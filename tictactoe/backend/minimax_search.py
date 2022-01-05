from game import Game
from math import  inf
from copy import deepcopy


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
    move = -inf
    for action in game.actions(state):
        value_2, action_2 = min_value(game, game.result(state, action))
    if value_2 > value:
        value, move = (value_2, action)
    return (value, move)


def min_value(game, state):
    if game.is_terminal(state):
        return (game.utility(state), None)
    value = inf
    move = inf
    for action in game.actions(state):
        value_2, action_2 = max_value(game, game.result(state, action))
    if value_2 < value:
        value, move = (value_2, action)
    return (value, move)


def print_board(board):
    for row in board:
        render_string = list(map(lambda x: " " if x == "" else x, row))
        print(render_string)


def game_thread_function():
    game = Game()
    board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
        ]
    
    while not game.is_terminal(state=board):
        if game.to_move(board) == "x":
            state = deepcopy(board)
            print("max moves")
            max_move = minimax_search(game=game, state=state)
            board = game.result(state=board, action=max_move)
            print_board(board)
        elif game.to_move(board) == "o":
            print("min moves")
            # here we need to recover a move from socket
            min_move = eval(input("Ingrese movimiento: "))
            board = game.result(state=board, action=min_move)
            print_board(board)


if __name__ == "__main__":
    game_thread_function()