#!/usr/bin/python3
"""Module defining the User class, which handles user-related data."""
from models.base_model import BaseModel


class User(BaseModel):
    """Subclass of BaseModel for representing user information.

    Attributes:
        email (str): User's email address.
        password (str): User's password.
        first_name (str): User's first name.
        last_name (str): User's last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
