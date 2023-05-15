"""
Module containing the "NetworkTraffic" Class.
"""

from typing import List

from ..host_traffic import HostTraffic
from ..protocol_traffic import ProtocolTraffic


class NetworkTraffic:
    """
    Class containing all the functionalities related to network traffic.
    """
    _pid: str
    _name: str
    _create_time: str
    _last_time_update: str
    _upload: str
    _download: str
    _upload_speed: str
    _download_speed: str
    _protocol_traffic: List[ProtocolTraffic]
    _host_traffic: List[HostTraffic]
