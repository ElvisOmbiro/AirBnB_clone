#!usr/bin/python3
"""Defines the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents Review

    Attributes:
        place_id(str) - place id
        user_id(str) - user id
        texr(str) - text
    """

    place_id = ""
    user_id = ""
    text = ""
