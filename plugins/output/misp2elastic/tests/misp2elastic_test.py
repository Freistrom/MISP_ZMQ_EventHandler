import unittest
import json
import os

from src.models.event import Event
from src.models.organisation import Organisation
from src.models.misp_object import MispObject
from src.models.galaxy import Galaxy
from src.models.attribute import Attribute
from ..misp2elastic import Misp2Elastic

class Misp2ElasticTest(unittest.TestCase):
    """Misp2Elastic plugin test cases."""

    @classmethod
    def setupClass(cls):
        try:
            event = open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates/create_event.json')))
            cls.event = json.load(event)
        except NameError as e:
            raise Exception('No Event Model Class defined!')

    @classmethod
    def teardownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_exec(self):
        event = Event.from_json(self, self.event)
        misp2elastic = Misp2Elastic();
        self.assertTrue(misp2elastic.exec(event))
