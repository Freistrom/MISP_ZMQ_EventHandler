from abc import ABC, abstractmethod

class Message(ABC):
    def __init__(self):
        super().__init__()

    @staticmethod
    def by_json(self, json):
        pass

    @staticmethod
    def to_json(self):
        pass
