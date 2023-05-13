"""
Module containing the "FlaskUI" Class.
"""

from flask import Flask


class FlaskUI:
    """
    Class to represent the User Interface using Flask.
    """
    _flask: Flask

    def __init__(self) -> None:
        """
        Constructor to set up some variables.
        """
        self._flask = Flask(__name__)
