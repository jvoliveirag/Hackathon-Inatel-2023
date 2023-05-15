"""
Module containing the "NetworkTrafficProvider" Interface.
"""

from abc import ABC, abstractmethod

from .network_traffic_provider_data import NetworkTrafficProviderData


class NetworkTrafficProvider(ABC):
    """
    Interface containing all the functionalities
    related to the network traffic provider.
    """

    @abstractmethod
    def get_data(self) -> NetworkTrafficProviderData:
        """
        Abstract Method to get the network traffic data.
        """
