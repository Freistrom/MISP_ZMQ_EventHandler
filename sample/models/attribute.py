from .model import Model
from .sighting import Sighting
import json
from inflection import underscore


class Attribute(Model):
    """The MISP Attribute Model"""

    def __init__(self):
        self.sightings = []
        self.shadow_attributes = []

    def from_json(self, attribute_json):
        attribute = Attribute()
        for key,value in attribute_json.items():
            if type(value) == list:
                for struct in value:
                    add = getattr(attribute, "add_{}".format(underscore(key)))
                    if key in ["ShadowAttribute"]:
                        add(Attribute.from_json(struct))
                    elif key in ["Sighting"]:
                        add(Sighting.from_json(struct))
            else:
                setattr(attribute,key,value)

        return attribute

    def add_shadow_attribute(self, shadow_attribute):
        self.shadow_attributes.append(attribute)

    def add_sighting(self, sighting):
        self.sightings.append(sighting)

    def to_json(self):
        return json.dumps(self.__dict__)
