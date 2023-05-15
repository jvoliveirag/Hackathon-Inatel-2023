"""
Module containing the "SocketIO" Class.

TODO: FIX MODULE
"""

from typing import Any
from collections import deque
import socket
import threading

from .constants import SERVER_ADDRESS
from domain.use_cases.network_traffic.interfaces import NetworkTrafficProvider


class SocketIO(NetworkTrafficProvider):
    """
    Class containing all sockets methods.
    """
    _is_active: bool = False
    _socket: socket.socket
    _messages: deque[Any] # TODO: FIX TYPE

    def __init__(self) -> None:
        """
        Constructor to set up some variables.
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._messages = deque()
        self._connect_to_server()

    def start(self) -> None:
        """"""
        self._is_active = True
        self._start_receiving_messages()

    def shut_down(self) -> None:
        """
        Method to shut down the client.
        """
        self._is_active = False
        self._receive_messages_thread.join()

    def get_data(self) -> Any:
        """
        Method to get the network traffic data.
        """
        self.shut_down()

        messages = self._get_all_messages_from_queue()

        self.start()

        return messages

    def _connect_to_server(self) -> None:
        """
        Private Method to connect to the server.

        TODO: LIDAR COM ConnectionRefusedError: [Errno 111] Connection refused
        when server is down
        """
        try:
            self._socket.connect(SERVER_ADDRESS)

        except socket.error as error:
            print(f"EXCEPTION: {error}")
            raise

    def _get_data_from_socket(self) -> Any:
        """
        """
        while self._is_active:
            message = self._socket.recv(1_048_576)
            decoded_message = message.decode()
            self._messages.append(decoded_message)

    def _start_receiving_messages(self):
        """
        """
        self._receive_messages_thread = threading.Thread(target=self._get_data_from_socket)
        self._receive_messages_thread.start()

    def _get_all_messages_from_queue(self):
        messages = []

        for message in self._messages:
            messages.append(message)

        self._messages.clear()

        return messages
