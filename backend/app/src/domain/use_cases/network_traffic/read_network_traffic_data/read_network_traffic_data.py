"""
Module containing the "ReadNetworkTrafficData" Class.
"""

from typing import List


from ....entities.network_traffic import NetworkTraffic
from ....models.response.read_network_traffic_data_response_model import ReadNetworkTrafficDataResponseModel
from ....dtos.network_traffic import NetworkTrafficDTO


class ReadNetworkTrafficData:
    """
    Class containing all the functionalities to get network traffic data.
    """

    def execute(self) -> ReadNetworkTrafficDataResponseModel:
        """
        Public Method to execute this use case by getting data from the server.
        """
        network_traffic = NetworkTraffic()
        network_data = network_traffic.get_data()

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
