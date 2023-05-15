"""
Module containing all the Flask constants.
"""

import os

from dotenv import load_dotenv


load_dotenv()

FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
