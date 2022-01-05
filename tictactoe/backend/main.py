import threading
from board import Board
from server import Server

# Threads construction
server_thread = threading.Thread(target=start_server)
game_thread = threading.Thread(target=start_game)

# Game move
game_move = None
move_event = threading.Event()


if __name__ == "__main__":
    server_thread.start()
