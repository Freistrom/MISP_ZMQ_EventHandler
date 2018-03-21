from .message import Message
import json


class Attribute(Message):
    """The MISP Event Model"""

    def from_json(self, json):
        attribute = Attribute()
        return attribute

    def to_json(self):
        return json.dumps(self.__dict__)
