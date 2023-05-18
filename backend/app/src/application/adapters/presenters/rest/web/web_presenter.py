"""
Module containing the "WebPresenter" Class.
"""

from typing import Any, Dict
from dataclasses import asdict

from domain.models.response.read_network_traffic_data_response_model import ReadNetworkTrafficDataResponseModel
from domain.models.response.read_network_traffic_average_speed_response_model import ReadNetworkTrafficAverageSpeedResponseModel


class WebPresenter:
    """
    TODO: FIX
    TODO: CAN USE ONLY ONE METHOD THAT RECEIVES A RESPONSE MODEL (CREATE INTERFACE FOR IT) AND CONVERT IT TO DICT
    """

    def present_network_traffic_data(self, response_model: ReadNetworkTrafficDataResponseModel) -> Dict[str, Any]:
        """
        """
        response_model_dict = asdict(response_model)

        return response_model_dict

    def present_network_traffic_average_speed(self, response_model: ReadNetworkTrafficAverageSpeedResponseModel) -> Dict[str, Any]:
        """
        """
        response_model_dict = asdict(response_model)

        return response_model_dict
