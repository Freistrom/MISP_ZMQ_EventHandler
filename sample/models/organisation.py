from .model import Model
from .logo import Logo
import json
from inflection import underscore
import pdb



class Organisation(Model):
    """The MISP Organisation Model"""

    def __init__(self):
        pass

    def from_json(self, organisation_json):
        organisation = Organisation()
        for key,value in organisation_json.items():
            if type(value) == dict:
                organisation.add_logo(Logo.from_json(self, value))
            else:
                setattr(organisation,key,value)

        return organisation

    def add_logo(self, logo):
        self.logo = logo

    def to_json(self):
        return json.dumps(self.__dict__)
