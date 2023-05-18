"""
Module containing the "DesktopPresenter" Class.
"""

from typing import Dict
from dataclasses import asdict

from domain.models.response.read_network_traffic_data_response_model import ReadNetworkTrafficDataResponseModel


class DesktopPresenter:
    """
    TODO: FIX
    """

    def present_network_traffic_data(self, response_model: ReadNetworkTrafficDataResponseModel) -> Dict[str, str]:
        """
        """
        response_model_dict = asdict(response_model)

        return response_model_dict
