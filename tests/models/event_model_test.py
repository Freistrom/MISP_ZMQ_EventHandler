from sample.models.event import Event
import unittest
import json
import os

class EventModelTest(unittest.TestCase):
    """Event Model test cases."""

    def setUp(self):
        try:
            msg = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/publish_event_msg.json'))).read()
            self.pub_event_msg = json.loads(msg)
        except NameError as e:
            raise Exception('No Event Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        event = Event.from_json(self, self.pub_event_msg)
        self.assertIsInstance(event, Event)
        self.assertTrue(hasattr(event, "id"))
        self.assertIs(event.id, 2)

if __name__ == '__main__':
   unittest.main()
