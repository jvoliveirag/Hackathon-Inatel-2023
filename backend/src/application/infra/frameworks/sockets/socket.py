"""
Module containing the "SocketIO" Class.
"""

from typing import Any
from queue import Queue
import socket
import sys
import threading

from .constants import SERVER_ADDRESS


class SocketIO:
    """
    Class containing all sockets methods.
    """
    _socket: socket.socket
    _queue: Queue[Any]

    def __init__(self) -> None:
        """
        Constructor to set up some variables.
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._queue = Queue()

    def start(self) -> None:
        """"""
        self._connect_to_server()

    def shut_down(self) -> None:
        """
        Method to shut down the client.
        """
        self._socket.close()
        sys.exit()

    def print_data(self):
        while True:
            msg = self._socket.recv(1024)
            print(msg)

    def get_data(self):
        """"""
        thread = threading.Thread(target=self._get_data_from_socket)
        thread.start()

    def _connect_to_server(self) -> None:
        """
        Private Method to connect to the server.
        """
        try:
            self._socket.connect(SERVER_ADDRESS)

        except socket.error as error:
            print(f"EXCEPTION: {error}")
            raise

    def _get_data_from_socket(self) -> Any:
        """
        """
        while True:
            msg = self._socket.recv(1024)
            self._queue.put(msg)
