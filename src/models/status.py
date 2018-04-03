from .model import Model
import json
from inflection import underscore


class Status(Model):
    """The MISP Status Model"""

    def __init__(self):
        pass

    def from_json(self, status_json):
        status = Status()
        for key,value in status_json.items():
            setattr(status,key,value)

        return status

    def to_json(self):
        return self.__dict__
