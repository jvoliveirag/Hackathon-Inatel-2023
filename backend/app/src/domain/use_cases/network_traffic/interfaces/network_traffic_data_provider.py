"""
Module containing the "NetworkTrafficDataProvider" Interface.
"""

from abc import ABC, abstractmethod


class NetworkTrafficDataProvider(ABC):
    """
    Interface containing all the functionalities
    related to the network traffic provider.
    """

    @abstractmethod
    def get_data(self) -> None: # TODO: FIX IMPORT
        """
        Abstract Method to get the network traffic data.
        """
