from .model import Model


class Tag(Message):
    """The MISP Galaxy Model"""

    def __init__(self):
        pass

    def from_json(self, json):
        tag = Tag()
        for key,value in json.items():
            setattr(tag,key,value)

        return tag

    def to_json(self):
        return json.dumps(self.__dict__)
