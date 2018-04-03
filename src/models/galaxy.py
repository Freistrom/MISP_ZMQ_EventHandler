from .model import Model
import json
from inflection import underscore


class Galaxy(Model):
    """The MISP Galaxy Model"""

    def __init__(self):
        pass

    def from_json(self, galaxy_json):
        galaxy = Galaxy()
        for key,value in galaxy_json.items():
            setattr(galaxy,key,value)

        return galaxy

    def to_json(self):
        return self.__dict__
