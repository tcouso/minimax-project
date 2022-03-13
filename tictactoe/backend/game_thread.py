from game import Game
from alpha_beta_search import alpha_beta_search
from copy import deepcopy


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

            # message passing mechanism pending

            max_move = None
            board = game.result(state=board, action=max_move)
        elif game.to_move(board) == "o":
            min_move = alpha_beta_search(game=game, state=state)
            board = game.result(state=board, action=min_move)


if __name__ == "__main__":
    game_thread_function()
