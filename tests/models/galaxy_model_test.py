from sample.models.galaxy import Galaxy
import unittest
import json
import os

class GalaxyModelTest(unittest.TestCase):
    """Event Model test cases."""

    def setUp(self):
        try:
            galaxy = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/galaxy.json')))
            self.galaxy = json.load(galaxy)
        except NameError as e:
            raise Exception('No Galaxy Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        galaxy = Galaxy.from_json(self, self.galaxy)
        self.assertIsInstance(galaxy, Galaxy)
        self.assertTrue(hasattr(galaxy, "id"))
        self.assertIs(galaxy.id, 1)

if __name__ == '__main__':
   unittest.main()
