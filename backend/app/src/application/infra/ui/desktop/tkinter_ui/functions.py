"""
Class containing all the button functions for the Tkinter UI.
"""

from application.adapters.controllers.desktop import DesktopController


def read_network_traffic_data():
    """
    TODO: FIX
    """
    controller = DesktopController()
    response = controller.get_network_traffic_data()

    return response
