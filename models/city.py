#!/usr/bin/python3
"""
This module define the City class
"""

from models import base_molde


class City(base_model.BaseModel):
    """
    This class represents a city.
    """

    state_id = ""
    name = ""
