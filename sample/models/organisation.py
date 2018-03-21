from .message import Message
import json


class Organisation(Message):
    """The MISP Event Model"""

    def from_json(self, json):
        organisation = Organisation()
        return organisation

    def to_json(self):
        return json.dumps(self.__dict__)
