from .message import Message
import json


class MispObject(Message):
    """The MISP Event Model"""

    def from_json(self, json):
        misp_object = MispObject()
        return misp_object

    def to_json(self):
        return json.dumps(self.__dict__)
