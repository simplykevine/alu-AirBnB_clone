#!/usr/bin/python3
"""This module defines the City class, which represents city objects."""

from models.base_model import BaseModel


class City(BaseModel):
    """This class manages city objects.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """
    state_id:
        str = '' 
    name:
        str = ''
