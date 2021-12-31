import zmq
from threading import Thread, Event

class Server():
    def __init__(self):
        self.inwards_message = None
        self.outwards_message = None
        self.inwards_message_event = Event()
        self.outwards_message_event = Event()
        self.__context = zmq.Context()
        self.__socket = self.__context.socket(zmq.REP)
        self.thread = Thread(target=self.run_server)

    def connect_server(self, port="tcp://*:5555"):
        self.__socket.bind(port)

    def inwards_message_deserialize(self, inwards_message):
        pass

    def outwards_message_serialize(self, outwards_message):
        pass

    def run_server(self):
        while True:
            # Waits request form client
            self.inwards_message = self.__socket.recv()
            self.inwards_message_event.set()
            # print("Inwards message event has been set!")
            

            # Waits for game update
            # self.__outwards_message_event.wait()

            # Send reply back to client
            self.__socket.send(b"World")
            self.inwards_message_event.clear()


if __name__ == "__main__":
    server = Server()
    server.connect_server()
    server.thread.start()
    server.inwards_message_event.wait()
    print(f"Received request: {server.inwards_message}")
