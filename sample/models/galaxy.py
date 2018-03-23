from .model import Model


class Galaxy(Message):
    """The MISP Galaxy Model"""

    def __init__(self):
        pass

    def from_json(self, json):
        galaxy = Galaxy()
        for key,value in json.items():
            setattr(galaxy,key,value)

        return galaxy

    def to_json(self):
        return json.dumps(self.__dict__)
