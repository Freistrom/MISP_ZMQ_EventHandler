from sample.models.sighting import Sighting
import unittest
import json
import os

class SightingModelTest(unittest.TestCase):
    """Event Model test cases."""

    def setUp(self):
        try:
            addition_msg = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/addition_sighting_msg.json'))).read()
            false_positive_msg = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/false_positive_sighting_msg.json'))).read()
            self.addition_msg = json.loads(addition_msg)
            self.false_positive_msg = json.loads(false_positive_msg)
        except NameError as e:
            raise Exception('No Sighting Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        sighting = Sighting.from_json(self, self.addition_msg)
        self.assertIsInstance(sighting, Sighting)
        self.assertTrue(hasattr(sighting, "id"))
        self.assertIs(sighting.id, 2)

if __name__ == '__main__':
   unittest.main()
