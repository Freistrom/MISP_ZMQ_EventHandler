from sample.models.misp_object import MispObject
import unittest
import json
import os


class MispObjectModelTest(unittest.TestCase):
    """Event Model test cases."""

    def setUp(self):
        try:
            misp_object = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/models/misp_object.json')))
            self.misp_object = json.load(misp_object)
        except NameError as e:
            raise Exception('No MispObject Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        misp_object = MispObject.from_json(self, self.misp_object)
        self.assertIsInstance(misp_object, MispObject)
        self.assertTrue(hasattr(misp_object, "id"))
        self.assertIs(misp_object.id, 1)

    def test_to_json(self):
        misp_object = MispObject.from_json(self, self.misp_object)
        self.assertDictEqual(misp_object.to_json(), self.misp_object)
