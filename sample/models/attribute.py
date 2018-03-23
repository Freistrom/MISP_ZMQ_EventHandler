from .model import Model


class Attribute(Message):
    """The MISP Attribute Model"""

    def __init__(self):
        self.sightings = []
        self.shadow_attributes = []

    def from_json(self, json):
        attribute = Attribute()
        for key,value in json.items():
            if type(value) == list:
                for struct in value.items():
                    add = getattr(event, "add_{}".format(underscore(key)))
                    if key in ["ShadowAttribute"]:
                        add(Attribute.from_json(struct))
                     if key in ["Sighting"]:
                        add(Sighting.from_json(struct))
            else
                setattr(attribute,key,value)

        return attribute

    def add_shadow_attribute(self, shadow_attribute):
        self.shadow_attributes.append(attribute)

    def add_sighting(self, sighting):
        self.sightings.append(sighting)

    def to_json(self):
        return json.dumps(self.__dict__)
