from .message import Message
import json


class Galaxy(Message):
    """The MISP Event Model"""

    def from_json(self, json):
        galaxy = Galaxy()
        return galaxy

    def to_json(self):
        return json.dumps(self.__dict__)
