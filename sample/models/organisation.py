from .model import Model


class Organisation(Message):
    """The MISP Organisation Model"""

    def __init__(self):
        pass

    def from_json(self, json):
        organisation = Organisation()
        for key,value in json.items():
            if type(value) == dict:
                organisation.add_logo(Logo.from_json(struct))
            else:
                setattr(organisation,key,value)

        return organisation

    def add_logo(self, logo):
        self.logo = logo

    def to_json(self):
        return json.dumps(self.__dict__)
