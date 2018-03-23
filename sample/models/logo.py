from .model import Model


class Logo(Model):
    """The MISP Organisation Model"""

    def __init__(self):
        pass

    def from_json(self, json):
        logo = Logo()
        for key,value in json.items():
            setattr(logo,key,value)

        return logo

    def to_json(self):
        return json.dumps(self.__dict__)
