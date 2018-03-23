from .model import Model


class Status(Message):
    """The MISP Status Model"""

    def __init__(self):
        pass

    def from_json(self, json):
        status = Status()
         for key,value in json.items():
            setattr(status,key,value)

        return status

    def to_json(self):
        return json.dumps(self.__dict__)
