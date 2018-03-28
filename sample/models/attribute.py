import json
from inflection import underscore
from inflection import singularize
from .model import Model
from .sighting import Sighting

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
                    add = getattr(attribute, "add_{}".format(singularize(underscore(key))))
                    if key in ["ShadowAttributes"]:
                        add(Attribute.from_json(struct))
                    elif key in ["Sightings"]:
                        add(Sighting.from_json(struct))
            else:
                setattr(attribute,key,value)

        return attribute

    def add_shadow_attribute(self, shadow_attribute):
        self.shadow_attributes.append(attribute)

    def add_sighting(self, sighting):
        self.sightings.append(sighting)

    def to_json(self):
        result = self.__dict__
        result['shadow_attributes'] = []
        result['sightings'] = []
        for shadow_attribute in self.shadow_attributes:
            result['shadow_attributes'].append(shadow_attribute.to_json())
        for sighting in self.sightings:
            result['sightings'].append(sighting.to_json())
        return result
