import unittest
import json
import os
from sample.models.model import Model


class ModelTest(unittest.TestCase):
    """Abstract Model test cases."""

    @classmethod
    def setupClass(cls):
        try:
            model = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/models/model.json')))
            cls.model = json.load(model)
        except NameError as e:
            raise Exception('No Model Class defined!')

    @classmethod
    def teardownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass  # clean up

    def test_from_json(self):
        model = Model.from_json(self, self.model)
        #self.assertIsInstance(model, Model)
        #self.assertTrue(hasattr(model, "id"))
        #self.assertIs(model.id, 2)

    def test_to_json(self):
        pass
