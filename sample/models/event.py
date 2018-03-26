import json
from inflection import underscore
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
                    add = getattr(event, "add_{}".format(underscore(key)))
                    if key in ["Attribute", "ShadowAttribute"]:
                        add(Attribute.from_json(self, struct))
                    elif key == "RelatedEvent":
                        add(Event.from_json(self, struct))
                    elif key == "Galaxy":
                        add(Galaxy.from_json(self, struct))
                    elif key == "Object":
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
        result['galaxies'] = self.galaxies.to_json()
        result['misp_objects'] = self.misp_objects.to_json()
        result['shadow_attributes'] = self.shadow_attributes.to_json()
        result['related_events'] = self.related_events.to_json()
        result['attributes'] = self.attributes.to_json()
        result['org'] = self.org.to_json()
        result['orgc'] = self.orgc.to_json()
        return result
