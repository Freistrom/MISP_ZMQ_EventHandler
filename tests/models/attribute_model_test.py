from sample.models.attribute import Attribute
import unittest
import json
import os


class AttributeModelTest(unittest.TestCase):
    """Event Model test cases."""

    def setUp(self):
        try:
            attribute = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/attribute.json')))
            self.attribute = json.load(attribute)
        except NameError as e:
            raise Exception('No Attribute Model Class defined!')

    def tearDown(self):
        pass

    def test_by_json(self):
        attribute = Attribute.from_json(self, self.attribute)
        self.assertIsInstance(attribute, Attribute)
        self.assertTrue(hasattr(attribute, "id"))
        #self.assertIs(attribute.id, 625)

if __name__ == '__main__':
   unittest.main()
