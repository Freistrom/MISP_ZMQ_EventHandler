from .model import Model
import json
from inflection import underscore


class Sighting(Model):
    """The MISP Sighting Model"""

    def __init__(self):
        pass

    def from_json(self, sighting_json):
        sighting = Sighting()
        for key,value in sighting_json.items():
            setattr(sighting,key,value)

        return sighting

    def to_json(self):
        return json.dumps(self.__dict__)
