import unittest
import json
import os
from sample.models.galaxy import Galaxy


class GalaxyModelTest(unittest.TestCase):
    """Event Model test cases."""

    @classmethod
    def setupClass(cls):
        try:
            galaxy = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/models/galaxy.json')))
            cls.galaxy = json.load(galaxy)
        except NameError as e:
            raise Exception('No Galaxy Model Class defined!')

    @classmethod
    def teardownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass  # clean up

    def test_from_json(self):
        galaxy = Galaxy.from_json(self, self.galaxy)
        self.assertIsInstance(galaxy, Galaxy)
        self.assertTrue(hasattr(galaxy, "id"))
        self.assertIs(galaxy.id, 1)

    def test_to_json(self):
        galaxy = Galaxy.from_json(self, self.galaxy)
        self.assertDictEqual(galaxy.to_json(), self.galaxy)
