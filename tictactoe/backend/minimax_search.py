from game import Game
from math import  inf
from copy import deepcopy

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
        state = deepcopy(board)
        if game.to_move(board) == "x":
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