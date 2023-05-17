"""
Module containing the "ReadNetworkTrafficDataUseCase" Class.

TODO: FIX MODULE
"""

from typing import List

from ..interfaces import NetworkTrafficDataProvider
from ....models.response.read_network_traffic_data_response_model import ReadNetworkTrafficDataResponseModel
from ....dtos.network_traffic import NetworkTrafficDTO


class ReadNetworkTrafficDataUseCase:
    """
    Class containing all the functionalities to get network traffic data.
    """
    _network_traffic_provider: NetworkTrafficDataProvider

    def __init__(self, network_traffic_provider: NetworkTrafficDataProvider) -> None:
        """
        Constructor to set up some variables.
        """
        self._network_traffic_provider = network_traffic_provider

    def execute(self) -> ReadNetworkTrafficDataResponseModel:
        """
        Public Method to execute this use case by getting data from the server.
        """
        network_data = self._network_traffic_provider.get_data()

        response = self._format_network_traffic_data(network_data)

        return response

    def _format_network_traffic_data(
        self,
        network_traffic_data: List[NetworkTrafficDTO]
    ) -> ReadNetworkTrafficDataResponseModel:
        """
        """
        response_model = ReadNetworkTrafficDataResponseModel(
            network_traffic_data=network_traffic_data
        )

        return response_model
