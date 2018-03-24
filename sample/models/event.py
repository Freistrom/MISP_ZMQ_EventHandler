from .model import Model
from .organisation import Organisation
from .misp_object import MispObject
from .galaxy import Galaxy
from .attribute import Attribute


import json
from inflection import underscore


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
        return json.dumps(self.__dict__)
