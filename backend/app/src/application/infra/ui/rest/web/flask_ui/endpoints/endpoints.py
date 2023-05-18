"""
Module containing all the endpoints for the Flask application.
"""

from application.adapters.controllers.rest.web import WebController

from flask import Response, jsonify


def index():
    """
    Function to render the index page.
    """
    return Response("Hello, World!")


def network_traffic_data():
    """
    Function to return the network traffic data.
    """
    controller = WebController()
    response = controller.get_network_traffic_data()

    return jsonify(response)


def network_traffic_average_speed():
    """
    """
    controller = WebController()
    response = controller.get_network_traffic_average_speed()

    return jsonify(response)
