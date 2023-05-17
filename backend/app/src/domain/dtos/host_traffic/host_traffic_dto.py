"""
Module containing the "HostTrafficDTO" Class.
"""

from dataclasses import dataclass


@dataclass
class HostTrafficDTO:
    """
    Class containing all the data for a Host Traffic.
    """
    host: str
    download: str
    upload: str
