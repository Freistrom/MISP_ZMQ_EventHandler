from .model import Model
import json
from inflection import underscore


class Tag(Model):
    """The MISP Galaxy Model"""

    def __init__(self):
        pass

    def from_json(self, tag_json):
        tag = Tag()
        for key,value in tag_json.items():
            setattr(tag,key,value)

        return tag

    def to_json(self):
        return json.dumps(self.__dict__)
