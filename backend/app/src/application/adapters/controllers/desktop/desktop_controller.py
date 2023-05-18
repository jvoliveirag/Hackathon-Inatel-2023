"""
Module containing the "DesktopController" Class.
"""

from application.adapters.presenters.desktop import DesktopPresenter
from dependencies.dependencies import network_traffic_provider_factory
from domain.use_cases.network_traffic.read_network_traffic_data import ReadNetworkTrafficDataUseCase


class DesktopController:
    """
    TODO
    """
    _presenter: DesktopPresenter

    def __init__(self) -> None:
        """
        TODO
        """
        self._presenter = DesktopPresenter()

    def get_network_traffic_data(self):
        """
        TODO
        """
        network_traffic_provider = network_traffic_provider_factory()
        network_traffic_provider.start()  # TODO: REMOVE

        use_case = ReadNetworkTrafficDataUseCase(network_traffic_provider)
        response = use_case.execute()

        desktop_response = self._presenter.present_network_traffic_data(response) 

        return desktop_response
