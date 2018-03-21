from abc import ABC, abstractmethod

class Message(ABC):
	def __init__(self):
        super(AbstractOperation, self).__init__()

    @abstractmethod
    def by_json(self, json):
        pass

    @abstractmethod
    def to_json(self):
    	pass