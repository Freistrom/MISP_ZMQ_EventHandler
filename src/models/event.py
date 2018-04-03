import json
from inflection import underscore
from inflection import singularize
from .model import Model
from .organisation import Organisation
from .misp_object import MispObject
from .galaxy import Galaxy
from .attribute import Attribute


class Event(Model):
    """The MISP Event Model"""

    def __init__(self):
        self.misp_objects = []
        self.attributes = []
        self.shadow_attributes = []
        self.galaxies = []
        self.related_events = []

    def from_json(self, event_json):
        event = Event()
        for key,value in event_json.items():
            if type(value) == dict:
                add_organistation = getattr(event, "add_{}".format(underscore(key)))
                add_organistation(Organisation.from_json(self, value))
            elif type(value) == list:
                for struct in value:
                    add = getattr(event, "add_{}".format(singularize(underscore(key))))
                    if key in ["Attributes", "ShadowAttributes"]:
                        add(Attribute.from_json(self, struct))
                    elif key == "RelatedEvents":
                        add(Event.from_json(self, struct))
                    elif key == "Galaxies":
                        add(Galaxy.from_json(self, struct))
                    elif key == "MispObjects":
                        event.add_misp_object(self, MispObject.from_json(self, struct))
            else:
                setattr(event,key,value)

        return event

    def add_misp_object(self, misp_object):
        self.misp_objects.append(misp_object)

    def add_galaxy(self, galaxy):
        self.galaxies.append(galaxy)

    def add_attribute(self, attribute):
        self.attributes.append(attribute)

    def add_shadow_attribute(self, shadow_attribute):
        self.shadow_attributes.append(attribute)

    def add_related_event(self, related_event):
        self.related_events.append(event)

    def add_org(self, org):
        self.org = org

    def add_orgc(self, orgc):
        self.orgc = orgc

    def to_json(self):
        result = self.__dict__
        result['galaxies'] = []
        result['misp_objects'] = []
        result['shadow_attributes'] = []
        result['related_events'] = []
        result['attributes'] = []

        for galaxy in self.galaxies:
            result['galaxies'].append(galaxy.to_json())

        for misp_object in self.misp_objects:
            result['misp_objects'].append(misp_object.to_json())

        for attribute in self.attributes:
            result['attributes'].append(attribute.to_json())

        for related_event in self.related_events:
            result['related_events'].append(related_event.to_json())

        for shadow_attribute in self.shadow_attributes:
            result['shadow_attributes'].append(shadow_attribute.to_json())

        result['org'] = self.org.to_json()
        result['orgc'] = self.orgc.to_json()
        return result
