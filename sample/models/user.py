from .model import Model


class User(Message):
    """The MISP User Model"""

    def __init__(self):
        pass

    def from_json(self, json):
        user = User()
        for key,value in json.items():
            setattr(user,key,value)

        return user

    def to_json(self):
        return json.dumps(self.__dict__)
