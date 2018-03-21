from .message import Message


class Event(Message):
    """The MISP Event Model"""

    def by_json(self, json):
        return Event()
