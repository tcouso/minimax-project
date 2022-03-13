import sys
from unittest import result

sys.path.append("backend")

from flask import Flask, render_template, request, jsonify
from game import Game
from alpha_beta_search import alpha_beta_search
from copy import deepcopy


app = Flask(__name__)
game = Game()
board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
    ]


@app.route("/")
def index(name=None):
    return render_template("index.html", name=name)

#  route for placing token


@app.route("/_place_token/<tuple:move>")
def place_token(move):
    x, y = move
    return f"coordenada x: {x} \n coordenada y: {y}"





@app.route("/hello")
def hello():
    return("Hello World!")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
