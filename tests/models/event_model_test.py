from sample.models.event import Event
import unittest

class EventModelTest(unittest.TestCase):
    """Event Model test cases."""
    def setUp(self):
        try:
            event =  Event.by_json(self, '"Event":{}')
        except NameError as e:
            pass

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        event = Event.by_json(self, '"Event":{}')
        self.assertIsInstance(event, Event)
        self.assertTrue(hasattr(event, "id"))
        self.assertIs(event.id, 1)

if __name__ == '__main__':
   unittest.main()
