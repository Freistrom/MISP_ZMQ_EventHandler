from abc import ABC, abstractmethod
import json
from inflection import underscore


class Model(ABC):

    def __init__(self):
        super().__init__()

    @staticmethod
    def from_json(self, json):
        pass

    @staticmethod
    def to_json(self):
        pass
