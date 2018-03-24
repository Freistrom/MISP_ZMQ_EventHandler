from .model import Model
import json
from inflection import underscore


class MispObject(Model):
    """The MISP Object Model"""

    def __init__(self):
        pass

    def from_json(self, misp_object_json):
        misp_object = MispObject()
        for key,value in misp_object_json.items():
            setattr(misp_object,key,value)

        return misp_object

    def to_json(self):
        return json.dumps(self.__dict__)
