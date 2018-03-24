from sample.models.model import Model
import unittest
import json
import os

class ModelTest(unittest.TestCase):
    """Event Model test cases."""

    def setUp(self):
        try:
            model = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/model.json')))
            self.model = json.load(model)
        except NameError as e:
            raise Exception('No Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        model = Model.from_json(self, self.model)
        #self.assertIsInstance(model, Model)
        #self.assertTrue(hasattr(model, "id"))
        #self.assertIs(model.id, 2)

if __name__ == '__main__':
   unittest.main()
