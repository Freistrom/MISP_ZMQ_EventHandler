from .model import Model
import json
from inflection import underscore
import pdb


class Logo(Model):
    """The MISP Logo Model"""

    def __init__(self):
        pass

    def from_json(self, logo_json):
        logo = Logo()
        for key,value in logo_json.items():
            setattr(logo,key,value)

        return logo

    def to_json(self):
        return json.dumps(self.__dict__)
