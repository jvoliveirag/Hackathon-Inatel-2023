"""
TODO: FIX
"""

from typing import List
from dataclasses import dataclass
from datetime import datetime


@dataclass
class NetworkTrafficAverageSpeedDTO:
    """"""
    pid: str
    name: str
    average_download_speed: float
    average_upload_speed: float
    last_time_update: datetime
    create_time: datetime
    downloads: List[float]
    uploads: List[float]
