"""
Class containing all the button functions for the Tkinter UI.

# TODO: FIX THIS MODULE
"""

from typing import Dict

from application.adapters.controllers.desktop import DesktopController


_controller = DesktopController()


def read_network_traffic_data() -> Dict[str, str]:
    """
    TODO: FIX
    """
    response = _controller.get_network_traffic_data()

    network_traffic_data = response.get("network_traffic_data")
    traffic_data = _format_network_traffic_data_to_plot_chart(network_traffic_data)

    return traffic_data


def save_chart():
    response = _controller.save_chart()
    print(response)


def export_chart():
    response = _controller.export_chart()
    print(response)


def _format_network_traffic_data_to_plot_chart(network_traffic_data):
    """
    TODO: FIX
    """
    traffic_data = {}

    for data in network_traffic_data:
        download_speed = data["download_speed"]
        name = data["name"]

        traffic_data[name] = download_speed

    return traffic_data
