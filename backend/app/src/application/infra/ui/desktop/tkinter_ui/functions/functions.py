"""
Class containing all the button functions for the Tkinter UI.

# TODO: FIX THIS MODULE
"""

from typing import Any, Dict, List

from application.adapters.controllers.desktop import DesktopController


_controller = DesktopController()


def read_network_traffic_data() -> Dict[str, str]:
    """
    TODO: FIX
    """
    response = _controller.get_network_traffic_data()

    network_traffic_data = response.get("network_traffic_data")

    return network_traffic_data


def read_network_traffic_average_speed() -> Dict[str, str]:
    """
    TODO FIX
    """
    response = _controller.get_network_traffic_average_speed()

    network_traffic_package = response.get("traffic_speed_averages")
    traffic_data = _format_network_traffic_data_to_plot_chart(network_traffic_package)

    return traffic_data


def _format_network_traffic_data_to_plot_chart(network_traffic_data: List[Dict[str, Any]]):
    """
    TODO: FIX
    """
    traffic_data = {}

    for data in network_traffic_data:
        name = data.get("name", "")
        average_download_speed = data.get("average_download_speed", 0.0)
        average_upload_speed = data.get("average_upload_speed", 0.0)

        traffic_data[name] = {
            "download": average_download_speed,
            "upload": average_upload_speed
        }

    return traffic_data
