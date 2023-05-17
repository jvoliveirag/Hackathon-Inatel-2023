"""
Module containing the "NetworkTrafficDTO" Class.
"""

from typing import List
from dataclasses import dataclass

from ..host_traffic import HostTrafficDTO
from ..protocol_traffic import ProtocolTrafficDTO


@dataclass
class NetworkTrafficDTO:
    """
    Class containing all the data for a Network Traffic.
    """
    pid: str
    name: str
    create_time: str
    last_time_update: str
    upload: str
    download: str
    upload_speed: str
    download_speed: str
    host_traffic: List[HostTrafficDTO]
    protocol_traffic: List[ProtocolTrafficDTO]
