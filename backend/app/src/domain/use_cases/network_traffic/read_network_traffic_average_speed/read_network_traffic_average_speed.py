"""
Module containing the "ReadNetworkTrafficAverageSpeed" Class.

TODO: FIX MODULE
"""

from typing import List
from collections import defaultdict
import re

from ....dtos.builders.network_traffic_average_speed import NetworkTrafficAverageSpeedDTOBuilder
from ....dtos.network_traffic import NetworkTrafficDTO
from ....dtos.network_traffic_average_speed import NetworkTrafficAverageSpeedDTO
from ....entities.network_traffic import NetworkTraffic
from ....models.response.read_network_traffic_average_speed_response_model import ReadNetworkTrafficAverageSpeedResponseModel


class ReadNetworkTrafficAverageSpeed:
    """
    Class containing all the functionalities to get network traffic data.
    """

    def execute(self) -> ReadNetworkTrafficAverageSpeedResponseModel:
        """
        Public Method to execute this use case by getting data from the server.
        """
        network_traffic = NetworkTraffic()
        network_traffic_data_package = network_traffic.get_data_package()

        response_model = self._get_response_model(network_traffic_data_package)

        return response_model

    def _get_response_model(
        self,
        network_traffic_data: List[NetworkTrafficDTO]
    ) -> ReadNetworkTrafficAverageSpeedResponseModel:
        """
        TODO
        """
        response = self._format_network_traffic_data(network_traffic_data)

        response_model = ReadNetworkTrafficAverageSpeedResponseModel(
            traffic_speed_averages=response
        )

        return response_model

    def _format_network_traffic_data(
        self,
        network_traffic_data: List[NetworkTrafficDTO]
    ) -> List[NetworkTrafficAverageSpeedDTO]:
        """
        """
        response_model = self._get_average_speeds(network_traffic_data)

        return response_model

    def _get_average_speeds(self, network_traffic_data: List[NetworkTrafficDTO]) -> List[NetworkTrafficAverageSpeedDTO]:
        """
        TODO: REFACTOR THIS METHOD
        """
        response: List[NetworkTrafficAverageSpeedDTO] = []

        speeds = self._sum_all_speeds(network_traffic_data)

        for pid, averages in speeds.items():
            self._calculate_averages(speeds, pid, averages)

        # Imprimir a velocidade média de download e upload para cada processo
        for pid, averages in speeds.items():
            dto = NetworkTrafficAverageSpeedDTOBuilder().build(pid, averages)

            response.append(dto)

        return response

    def _sum_all_speeds(self, network_traffic_data: List[NetworkTrafficDTO]):
        """
        TODO: REFACTOR
        """
        speeds = defaultdict(lambda: {"download_average": 0.0, "upload_average": 0.0, "process_count": 0, "downloads": [], "uploads": []})

        for data in network_traffic_data:
            pid = data.pid
            d = self._format_speed_to_float(data.download_speed)
            u = self._format_speed_to_float(data.upload_speed)

            speeds[pid]["downloads"].append(d)
            speeds[pid]["uploads"].append(u)
            speeds[pid]["download_average"] += d
            speeds[pid]["upload_average"] += u
            speeds[pid]["process_count"] += 1
            speeds[pid]["name"] = data.name
            speeds[pid]["last_time_update"] = data.last_time_update
            speeds[pid]["create_time"] = data.create_time

        return speeds

    def _calculate_averages(self, speeds, pid, averages):
        """
        TODO: REFACTOR
        """
        downloads_sum = averages["download_average"]
        uploads_sum = averages["upload_average"]

        amount = speeds[pid]["process_count"]

        speeds[pid]["download_average"] = downloads_sum / amount
        speeds[pid]["upload_average"] = uploads_sum / amount

    def _format_speed_to_float(self, speed: str) -> float:
        """
        TODO
        """
        units = {
            'B/s': 1,
            'KB/s': 1024,
            'MB/s': 1024 ** 2,
            'GB/s': 1024 ** 3
        }

        pattern = r'(\d+\.?\d*)([KMG]?B\/s)'
        match = re.match(pattern, speed)

        if not match:
            return 0.0

        value = float(match.group(1))
        unit = match.group(2)

        speed_number = value * units[unit]


        return speed_number
