from .message import Message
import json
from inflection import underscore


class Event(Message):
    """The MISP Event Model"""

    def __init__(self):
        self.misp_object = []
        self.attribute = []
        self.shadow_attribute = []
        self.galaxy = []
        self.related_event = []

    def from_json(self, json):
        event = Event()
        for key,value in json['Event'].items():
            if type(value) in [dict, list]:
                if key in ["Org", "Orgc"]:
                    if key == "Org"
                        event.add_org_from_json(value)
                    else
                        event.add_orgc_from_json(value)
                else if key in ["Attribute", "ShadowAttribute"]:
                    for attr in value:
                        if key == "Attribute"
                            event.add_attribute_from_json(attr)
                        else
                            event.add_shadow_attribute_from_json(attr)
                else if key == "RelatedEvent":
                    for evt in value:
                        event.add_related_event_from_json(evt)
                else if key == "Galaxy":
                    for glx in value:
                        event.add_galaxy_from_json(glx)
                else if key == "Object":
                    for obj in value:
                        event.add_object_from_json(obj)
            else:
                setattr(event,key,value)
        return event

    def add_misp_object(self, misp_object):
        self.misp_object.append(misp_object)

    def add_galax(self, galaxy):
        self.galaxy.append(galaxy)

    def add_attribute(self, attribute):
        self.attribute.append(attribute)

    def add_shadow_attribute(self, shadow_attribute):
        self.shadow_attribute.append(attribute)

    def add_related_event(self, related_event):
        self.related_event.append(event)

    def add_org(self, org):
        self.org.append(org)

    def add_orgc(self, orgc):
        self.orgc.append(orgc)

    def add_misp_object_from_json(self, misp_object):
        misp_object = MispObject.from_json(misp_object)
        self.add_object(misp_object)

    def add_galax_from_json(self, galaxy):
        galaxy = Galxy.from_json(galaxy)
        self.add_galaxy(galaxy)

    def add_attribute_from_json(self, attribute):
        attribute = Attribute.from_json(attribute)
        self.add_attribute(attribute)

    def add_shadow_attribute_from_json(self, shadow_attribute):
        shadow_attribute = Attribute.from_json(attribute)
        self.add_shadow_attribute(shadow_attribute)

    def add_related_event_from_json(self, related_event):
        related_event = Event.from_json(event)
        self.add_related_event(related_event)

    def add_org_from_json(self, org):
        org = Organisation.from_json(org)
        self.add_org(org)

    def add_orgc_from_json(self, orgc):
        orgc = MispObject.from_json(orgc)
        self.add_orgc(orgc)

    def to_json(self):
        return json.dumps(self.__dict__)
