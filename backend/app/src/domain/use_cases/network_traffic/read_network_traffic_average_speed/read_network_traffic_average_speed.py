"""
Module containing the "ReadNetworkTrafficAverageSpeed" Class.

TODO: FIX MODULE
"""

from typing import List
from collections import defaultdict
from datetime import datetime

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
        speeds = defaultdict(lambda: {"download_average": 0.0, "upload_average": 0.0, "process_count": 0})

        for data in network_traffic_data:
            self._sum_all_speeds(speeds, data)

        for pid, averages in speeds.items():
            self._calculate_averages(speeds, pid, averages)

        # Imprimir a velocidade média de download e upload para cada processo
        for pid, averages in speeds.items():
            dto = self._create_average_speed_dto(averages, pid)

            response.append(dto)

        return response

    def _sum_all_speeds(self, speeds, data):
        """
        TODO: REFACTOR
        """
        pid = data.pid
        d = self._format_speed_to_float(data.download_speed)
        u = self._format_speed_to_float(data.upload_speed)

        speeds[pid]["download_average"] += d
        speeds[pid]["upload_average"] += u
        speeds[pid]["process_count"] += 1
        speeds[pid]["name"] = data.name
        speeds[pid]["last_time_update"] = data.last_time_update
        speeds[pid]["create_time"] = data.create_time

    def _calculate_averages(self, speeds, pid, averages):
        """
        TODO: REFACTOR
        """
        downloads_sum = averages["download_average"]
        uploads_sum = averages["upload_average"]

        amount = speeds[pid]["process_count"]

        speeds[pid]["download_average"] = downloads_sum / amount
        speeds[pid]["upload_average"] = uploads_sum / amount

    def _create_average_speed_dto(self, averages, pid):
        """
        """
        name = averages.get("name", "")
        average_download_speed = averages.get("download_average", 0.0)
        average_upload_speed = averages.get("upload_average", 0.0)
        last_time_update = averages.get("last_time_update", datetime.now())
        create_time = averages.get("create_time", datetime.now())

        dto = NetworkTrafficAverageSpeedDTO(
            pid=pid,
            name=name,
            average_download_speed=average_download_speed,
            average_upload_speed=average_upload_speed,
            last_time_update=last_time_update,
            create_time=create_time
        )

        return dto

    def _format_speed_to_float(self, speed: str) -> float:
        """
        TODO
        """
        speed_without_unit = speed[:-3]

        # TODO: FIX ERROR BELOW
        # ValueError: could not convert string to float: '1.26K'
        try:
            speed_int = float(speed_without_unit)
        except ValueError:
            speed_int = 0.0

        return speed_int
