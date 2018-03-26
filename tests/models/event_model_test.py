import unittest
import json
import os
from sample.models.event import Event
from sample.models.organisation import Organisation
from sample.models.misp_object import MispObject
from sample.models.galaxy import Galaxy
from sample.models.attribute import Attribute



class EventModelTest(unittest.TestCase):
    """Event Model test cases."""

    def setUp(self):
        try:
            event = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/models/event.json')))
            self.event = json.load(event)
        except NameError as e:
            raise Exception('No Event Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        event = Event.from_json(self, self.event)
        self.assertIsInstance(event, Event)
        self.assertTrue(hasattr(event, "id"))
        self.assertIs(event.id, 2)
