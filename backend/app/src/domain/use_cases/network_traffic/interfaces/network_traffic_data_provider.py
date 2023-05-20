"""
Module containing the "NetworkTrafficDataProvider" Interface.
"""

from typing import List
from abc import ABC, abstractmethod

from ....dtos.network_traffic import NetworkTrafficDTO

class NetworkTrafficDataProvider(ABC):
    """
    Interface containing all the functionalities
    related to the network traffic provider.
    """

    @abstractmethod
    def start(self) -> None:
        """
        Abstract Method to start the client.
        """

    @abstractmethod
    def get_data(self) -> List[NetworkTrafficDTO]:
        """
        Abstract Method to get a single network traffic data.
        """

    @abstractmethod
    def get_data_package(self) -> List[NetworkTrafficDTO]:
        """
        Abstract Method to get the network traffic data package (collection of data).
        """
