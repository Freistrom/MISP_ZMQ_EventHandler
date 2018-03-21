from .message import Message
import json


class User(Message):
    """The MISP Event Model"""

    def from_json(self, json):
        user = User()
        return user

    def to_json(self):
        return json.dumps(self.__dict__)
