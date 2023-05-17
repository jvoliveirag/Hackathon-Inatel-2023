"""
Module containing the "ProtocolTrafficDTO" Class.
"""

from dataclasses import dataclass


@dataclass
class ProtocolTrafficDTO:
    """
    Class containing all the data for a Protocol Traffic.
    """
    protocol: str
    download: str
    upload: str
