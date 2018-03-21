from abc import ABC, abstractmethod

class Plugin(ABC):
    def __init__(self):
        super().__init__()

    @staticmethod
    def load(self, json):
        pass

    @staticmethod
    def exec(self, json):
        pass

    @staticmethod
    def before_hook(self, json):
        pass

    @staticmethod
    def after_hook(self, json):
        pass
