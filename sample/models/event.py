from .message import Message
import json


class Event(Message):
    """The MISP Event Model"""

    def by_json(self, json):
        event = Event()
        #for misp_event in json:
        event.id = json["Event"]["id"]
        return event
