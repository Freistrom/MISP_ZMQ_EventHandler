from sample.models.sighting import Sighting
import unittest
import json
import os

class SightingModelTest(unittest.TestCase):
    """Sighting Model test cases."""

    def setUp(self):
        try:
            sighting = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/sighting.json')))
            self.sighting = json.load(sighting)
        except NameError as e:
            raise Exception('No Sighting Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        sighting = Sighting.from_json(self, self.sighting)
        self.assertIsInstance(sighting, Sighting)
        self.assertTrue(hasattr(sighting, "id"))
        self.assertIs(sighting.id, 1)

if __name__ == '__main__':
   unittest.main()
