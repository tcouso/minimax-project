# Implementation of the api based on: https://www.youtube.com/watch?v=GMppyAPbLYk
import json
from flask import Flask
from flask_restful import Api, Resource, reqparse
from alpha_beta_search import alpha_beta_search
from game import Game


app = Flask(__name__)
api = Api(app)


move_post_args = reqparse.RequestParser()
move_post_args.add_argument("board", type=str, help="Board state", required=True)


game = Game()

class MinimaxAgent(Resource):
    def put(self):
        args = move_post_args.parse_args()
        board = json.loads(args["board"])
        agent_move = alpha_beta_search(game=game, state=board)
        new_board = game.result(state=board, action=agent_move)

        return json.dumps(new_board)


api.add_resource(MinimaxAgent, "/move")

if __name__ == "__main__":
    app.run(debug=True)
