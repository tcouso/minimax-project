from game import Game
from minimax_search import minimax_search
from copy import deepcopy


def print_board(board):
    for row in board:
        render_string = list(map(lambda x: " " if x == "" else x, row))
        print(render_string)


def game_thread_function():
    """ Command line interface for tic-tac-toe"""
    game = Game()
    board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
        ]
    print("TIC TAC TOE")
    print_board(board)
    
    while not game.is_terminal(state=board):
        state = deepcopy(board)
        if game.to_move(board) == "x":
            print("max moves")
            max_move = eval(input("Ingrese movimiento: "))
            # max_move = minimax_search(game=game, state=state)
            board = game.result(state=board, action=max_move)
            print_board(board)
        elif game.to_move(board) == "o":
            print("min moves")
            # min_move = eval(input("Ingrese movimiento: "))
            min_move = minimax_search(game=game, state=state)
            board = game.result(state=board, action=min_move)
            print_board(board)


if __name__ == "__main__":
    game_thread_function()