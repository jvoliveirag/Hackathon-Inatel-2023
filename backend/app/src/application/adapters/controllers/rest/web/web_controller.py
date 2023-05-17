"""
Module containing the "WebController" Class.
"""

from application.adapters.presenters.rest.web import WebPresenter
from dependencies.dependencies import network_traffic_provider_factory
from domain.use_cases.network_traffic.read_network_traffic_data import ReadNetworkTrafficDataUseCase


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
        network_traffic_provider = network_traffic_provider_factory()
        network_traffic_provider.start()

        use_case = ReadNetworkTrafficDataUseCase(network_traffic_provider)
        response = use_case.execute()

        web_response = self._presenter.present_network_traffic_data(response)

        return web_response
