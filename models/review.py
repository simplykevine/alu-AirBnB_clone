#!/usr/bin/python3
"""Module defining a Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class represents a review object.

    Attributes:
        place_id (str): The ID of the place
        associated with the review.
        user_id (str): The ID of the user who
        created the review.
        text (str): The text content of the review.
    """

    place_id:
        str = ''
    user_id:
        str = ''
    text:
        str = ''
