#!/usr/bin/python3
"""defines available Amenities"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents amenities

    Attributes:
        name(str) - name of Amenity
        """
    name = ""
