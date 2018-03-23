from .model import Model


class MispObject(Message):
    """The MISP Object Model"""

    def __init__(self):
        pass

    def from_json(self, json):
        misp_object = MispObject()
        for key,value in json.items():
            setattr(misp_object,key,value)

        return misp_object

    def to_json(self):
        return json.dumps(self.__dict__)
