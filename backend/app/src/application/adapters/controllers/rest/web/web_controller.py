"""
Module containing the "WebController" Class.
"""

from application.adapters.presenters.rest.web import WebPresenter
from domain.use_cases.network_traffic.read_network_traffic_data import ReadNetworkTrafficData
from domain.use_cases.network_traffic.read_network_traffic_average_speed import ReadNetworkTrafficAverageSpeed


class WebController:
    """
    TODO: FIX
    """
    _presenter: WebPresenter

    def __init__(self) -> None:
        """
        """
        self._presenter = WebPresenter()

    def get_network_traffic_data(self):
        """
        """
        use_case = ReadNetworkTrafficData()
        response = use_case.execute()

        web_response = self._presenter.present_network_traffic_data(response)

        return web_response

    def get_network_traffic_average_speed(self):
        """
        """
        use_case = ReadNetworkTrafficAverageSpeed()
        response = use_case.execute()

        web_response = self._presenter.present_network_traffic_average_speed(response)

        return web_response
