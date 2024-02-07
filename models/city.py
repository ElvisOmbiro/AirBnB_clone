#!usr/bin/python3
"""Defines the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents the City

    Attributes:
        state_id(str) - state's id
        name(str) - name of the city
    """

    state_id = ""
    name = ""

