from .message import Message
import json


class Sighting(Message):
    """The MISP Event Model"""

    def from_json(self, json):
        sighting = Sighting()
        return sighting

    def to_json(self):
        return json.dumps(self.__dict__)
