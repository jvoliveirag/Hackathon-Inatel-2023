"""
Module containing the "UI" Interface.
"""

from abc import ABC, abstractmethod

class UI(ABC):
    """
    Interface to represent a "UI".
    """

    @abstractmethod
    def execute(self) -> None:
        """
        Abstract Method to execute the UI.
        """
