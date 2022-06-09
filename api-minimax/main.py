from flask import Flask, json, request
from flask_cors import CORS
from alpha_beta_search import alpha_beta_search
from game import Game

app = Flask(__name__)
CORS(app)
game = Game()


@app.route("/move", methods=["POST"])
def compute_move():
    raw_board = json.loads(request.data)["board"]
    board = [raw_board[0:3], raw_board[3:6], raw_board[6:9]]
    agent_move = alpha_beta_search(game=game, state=board)
    new_board_raw = game.result(state=board, action=agent_move)
    new_board = new_board_raw[0] + new_board_raw[1] + new_board_raw[2]
    response = json.dumps({"new-board": new_board})
    return response


if __name__ == "__main__":
    app.run(debug=True)
