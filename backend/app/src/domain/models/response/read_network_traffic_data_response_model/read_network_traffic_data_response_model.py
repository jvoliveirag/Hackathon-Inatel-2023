"""
TODO: FIX MODULE AND PACKAGE NAMING
"""

from typing import List
from dataclasses import dataclass

from ....dtos.network_traffic import NetworkTrafficDTO


@dataclass
class ReadNetworkTrafficDataResponseModel:
    """
    TODO: ADD DOCSTRING
    """
    network_traffic_data: List[NetworkTrafficDTO]
