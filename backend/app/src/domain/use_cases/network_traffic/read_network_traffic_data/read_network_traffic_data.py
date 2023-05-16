"""
Module containing the "ReadNetworkTrafficData" Class.

TODO: FIX MODULE
"""

import json
from typing import Any

from ..interfaces import NetworkTrafficDataProvider


class ReadNetworkTrafficData:
    """
    Class containing all the functionalities to get network traffic data.
    """
    _network_traffic_provider: NetworkTrafficDataProvider

    def __init__(self, network_traffic_provider: NetworkTrafficDataProvider) -> None:
        """
        Constructor to set up some variables.
        """
        self._network_traffic_provider = network_traffic_provider

    def execute(self) -> Any:
        """
        Public Method to execute this use case by getting data from the server.
        """
        network_data = self._network_traffic_provider.get_data()

        return network_data
