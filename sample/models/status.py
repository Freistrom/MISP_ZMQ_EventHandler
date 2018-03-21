from .message import Message
import json


class Status(Message):
    """The MISP Event Model"""

    def from_json(self, json):
        status = Status()
        return status

    def to_json(self):
        return json.dumps(self.__dict__)
