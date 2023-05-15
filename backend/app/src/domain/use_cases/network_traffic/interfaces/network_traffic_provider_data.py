"""
Module containing the "NetworkTrafficProviderData" DataStructure.
"""

from typing import List
from dataclasses import dataclass

from domain.entities.host_traffic import HostTraffic
from domain.entities.protocol_traffic import ProtocolTraffic


@dataclass
class NetworkTrafficProviderData:
    """
    DataStructure containing all the network traffic provider data.
    """
    pid: str
    name: str
    create_time: str
    last_time_update: str
    upload: str
    download: str
    upload_speed: str
    download_speed: str
    protocol_traffic: List[ProtocolTraffic]
    host_traffic: List[HostTraffic]
