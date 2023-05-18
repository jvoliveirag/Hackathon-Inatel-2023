"""
Module containing the "SocketIO" Class.

TODO: MOVE PARSERS AND FORMATTERS TO INTERFACE ADAPTERS LAYER
TODO: IF FUNCTION TO ALWAYS RETURN IS IMPLEMENTEND, REMOVE THE AUTOMATICALLY START
"""

from typing import Dict, List
from collections import deque
import json
import socket
import threading

from .constants import SERVER_ADDRESS
from domain.builders.network_traffic_dto_builder import NetworkTrafficDTOBuilder
from domain.dtos.network_traffic import NetworkTrafficDTO
from domain.use_cases.network_traffic.interfaces import NetworkTrafficDataProvider


class SocketIO(NetworkTrafficDataProvider):
    """
    Class containing all sockets methods.
    """
    _is_active: bool
    _socket: socket.socket
    _messages: deque[NetworkTrafficDTO]

    def __init__(self) -> None:
        """
        Constructor to set up some variables.
        """
        self._is_active = False
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._messages = deque()
        self._connect_to_server()

        # TODO: REMOVE BELOW IF CONDITIONS ON MODULE DOCSTRING MET
        self.start()

    def start(self) -> None:
        """"""
        self._is_active = True
        self._start_thread_to_receive_messages()

    def shut_down(self) -> None:
        """
        Method to shut down the client.
        """
        self._is_active = False
        self._receive_messages_thread.join()

    def get_data(self) -> List[NetworkTrafficDTO]:
        """
        Method to get the network traffic data.
        """
        self.shut_down()

        messages = self._get_all_messages_from_queue()

        return messages

    def _connect_to_server(self) -> None:
        """
        Private Method to connect to the server.

        TODO: DEAL WITH
        ConnectionRefusedError: [Errno 111] Connection refused
        when server is down
        """
        try:
            self._socket.connect(SERVER_ADDRESS)

        except socket.error as error:
            print(f"EXCEPTION: {error}")
            raise

    def _get_all_messages_from_queue(self) -> List[NetworkTrafficDTO]:
        messages = list(self._messages)

        self._messages.clear()

        return messages

    def _start_thread_to_receive_messages(self):
        """
        """
        self._receive_messages_thread = threading.Thread(target=self._get_messages_from_socket)
        self._receive_messages_thread.start()

    def _get_messages_from_socket(self) -> None:
        """
        """
        while self._is_active:
            MESSAGE_SIZE = 10 * 1024
            message = self._socket.recv(MESSAGE_SIZE)
            decoded_message = message.decode()

            self._store_message_on_queue(decoded_message)

    def _store_message_on_queue(self, message: str) -> None:
        """
        TODO IMPLEMENT
        """
        if not message:
            return

        bodies = self._parse_message_into_bodies(message)
        json_payloads = self._format_bodies_into_json(bodies)

        for json_payload in json_payloads:
            network_traffic_dto = self._build_network_traffic_dto(json_payload)

            if network_traffic_dto:
                self._messages.append(network_traffic_dto)

    def _parse_message_into_bodies(self, payload: str) -> List[str]:
        """
        TODO IMPLEMENT
        """
        HEADER = "HTTP/1.1 200 OK"
        bodies: List[str] = []
        data = payload.split(HEADER)

        if not data:
            return bodies

        is_single_message = len(data) == 2
        if is_single_message:
            _, body = data[1].split("\r\n\r\n")
            bodies.append(body)
            return bodies

        data_without_first_header = data[1:]
        for body_with_header in data_without_first_header:
            body, _ = body_with_header.split(HEADER)
            bodies.append(body)

        return bodies

    def _format_bodies_into_json(self, bodies: List[str]) -> List[Dict[str, str]]:
        """
        TODO IMPLEMENT
        """
        json_messages: List[Dict[str, str]] = []

        for body in bodies:
            json_message: List[Dict[str, str]] = json.loads(body)
            json_messages.extend(json_message)

        return json_messages

    def _build_network_traffic_dto(self, payload: Dict[str, str]) -> NetworkTrafficDTO:
        """
        TODO IMPLEMENT
        """
        network_traffic_dto = NetworkTrafficDTOBuilder().build(payload)

        return network_traffic_dto
