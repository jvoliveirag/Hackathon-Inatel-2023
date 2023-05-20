"""
Module containing the "NetworkTraffic" Class.
"""

from typing import List

from dependencies import network_traffic_provider_factory
from domain.dtos.network_traffic import NetworkTrafficDTO
from domain.use_cases.network_traffic.interfaces import NetworkTrafficDataProvider


class NetworkTraffic:
    """
    Class containing all the functionalities to handle the network traffic.
    """
    _network_traffic_data_provider: NetworkTrafficDataProvider

    def __init__(self) -> None:
        """
        Constructor to set up some variables.
        """
        self._network_traffic_data_provider = network_traffic_provider_factory()

    def get_data(self) -> List[NetworkTrafficDTO]:
        """
        Public Method to get the network traffic data.
        """
        network_traffic_data = self._network_traffic_data_provider.get_data()

        return network_traffic_data

    def get_data_package(self) -> List[NetworkTrafficDTO]:
        """
        Public Method to get the network traffic data package.
        """
        network_traffic_data_package = self._network_traffic_data_provider.get_data_package()

        return network_traffic_data_package
