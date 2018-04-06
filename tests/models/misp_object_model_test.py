import unittest
import json
import os
from src.models.misp_object import MispObject


class MispObjectModelTest(unittest.TestCase):
    """MispObject Model test cases."""

    @classmethod
    def setupClass(cls):
        try:
            misp_object = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/models/misp_object.json')))
            cls.misp_object = json.load(misp_object)
        except NameError as e:
            raise Exception('No MispObject Model Class defined!')

    @classmethod
    def teardownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass  # clean up

    def test_from_json(self):
        misp_object = MispObject.from_json(self, self.misp_object)
        self.assertIsInstance(misp_object, MispObject)
        self.assertTrue(hasattr(misp_object, "id"))
        self.assertIs(misp_object.id, 1)

    def test_to_json(self):
        misp_object = MispObject.from_json(self, self.misp_object)
        self.assertDictEqual(misp_object.to_json(), self.misp_object)
