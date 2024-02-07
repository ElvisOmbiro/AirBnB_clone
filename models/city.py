#!usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """Represents the City

    Attributes:
        state_id(str) - state's id
        name(str) - name of the city
    """

    state_id = ""
    name = ""

