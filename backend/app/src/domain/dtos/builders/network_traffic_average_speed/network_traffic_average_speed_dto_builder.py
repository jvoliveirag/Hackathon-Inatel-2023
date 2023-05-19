"""
TODO IMPLEMENT
"""

from typing import Dict, Union
from datetime import datetime

from domain.dtos.network_traffic_average_speed import NetworkTrafficAverageSpeedDTO

class NetworkTrafficAverageSpeedDTOBuilder:
    """
    TODO IMPLEMENT
    """

    @staticmethod
    def build(pid: str, network_traffic_average_data: Dict[str, Union[str, float, datetime]]) -> NetworkTrafficAverageSpeedDTO:
        """
        TODO IMPLEMENT
        """
        name: str = network_traffic_average_data.get("name", "")  # type: ignore
        average_download_speed: float = network_traffic_average_data.get("download_average", 0.0)  # type: ignore
        average_upload_speed: float = network_traffic_average_data.get("upload_average", 0.0)  # type: ignore
        last_time_update: datetime = network_traffic_average_data.get("last_time_update", datetime.now())  # type: ignore
        create_time: datetime = network_traffic_average_data.get("create_time", datetime.now())  # type: ignore
        downloads = network_traffic_average_data.get("downloads", [])  # type: ignore
        uploads = network_traffic_average_data.get("uploads", [])  # type: ignore

        dto = NetworkTrafficAverageSpeedDTO(
            pid=pid,
            name=name,
            average_download_speed=average_download_speed,
            average_upload_speed=average_upload_speed,
            last_time_update=last_time_update,
            create_time=create_time,
            downloads=downloads,
            uploads=uploads
        )

        return dto
