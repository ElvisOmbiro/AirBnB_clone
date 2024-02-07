#!/usr/bin/python3
"""Defines the State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents the state

    Attributes:
        name(str) - name state
    """
    name = ""
