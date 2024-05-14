#!/usr/bin/python3
"""
This module defines the State class,
which manages state objects.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Subclass of BaseModel for representing
    and handling state information.

    Attributes:
        name (str): The name of the state.
    """
    name = ""
