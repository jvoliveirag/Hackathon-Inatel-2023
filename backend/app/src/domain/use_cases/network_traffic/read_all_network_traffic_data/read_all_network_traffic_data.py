"""
Module containing the "ReadAllNetworkTrafficData" Class.

TODO: FIX MODULE
"""

import json
from typing import Any

from ..interfaces import NetworkTrafficProvider


class ReadAllNetworkTrafficData:
    """
    Class containing all the functionalities to get network traffic data.
    """
    _network_traffic_provider: NetworkTrafficProvider

    def __init__(self, network_traffic_provider: NetworkTrafficProvider) -> None:
        """
        Constructor to set up some variables.
        """
        self._network_traffic_provider = network_traffic_provider

    def execute(self) -> Any:
        """
        Public Method to execute this use case by getting data from the server.
        """
        network_data = self._network_traffic_provider.get_data()

        response = self._get_formatted_data(network_data)

        return response

    def _get_formatted_data(self, network_traffic_provider_data: list[str]) -> Any:
        """
        TODO: FIX METHOD

        # TEM ALGUM B.O. AQUI.
        # SERÁ QUE É PORQUE A LISTA (network_traffic_provider_data) ESTÁ VINDO VAZIA?
        """
        for payload in network_traffic_provider_data:
            # Step 1
            try:
                header, data = payload.split("\r\n\r\n")
            except Exception:
                import pdb; pdb.set_trace()
            # Step 2
            traffics = json.loads(data)

        return traffics
