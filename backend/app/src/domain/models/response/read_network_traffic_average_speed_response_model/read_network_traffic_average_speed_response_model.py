"""
TODO: FIX MODULE AND PACKAGE NAMING
"""

from typing import List
from dataclasses import dataclass

from domain.dtos.network_traffic_average_speed import NetworkTrafficAverageSpeedDTO


@dataclass
class ReadNetworkTrafficAverageSpeedResponseModel:
    """
    TODO: ADD DOCSTRING
    """
    traffic_speed_averages: List[NetworkTrafficAverageSpeedDTO]
