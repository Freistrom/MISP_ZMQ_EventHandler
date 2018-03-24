from .model import Model
import json
from inflection import underscore


class User(Model):
    """The MISP User Model"""

    def __init__(self):
        pass

    def from_json(self, user_json):
        user = User()
        for key,value in user_json.items():
            setattr(user,key,value)

        return user

    def to_json(self):
        return json.dumps(self.__dict__)
