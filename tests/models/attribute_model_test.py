from sample.models.attribute import Attribute
import unittest
import json
import os

class AttributeModelTest(unittest.TestCase):
    """Event Model test cases."""

    def setUp(self):
        try:
            create_msg = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/create_attribute_msg.json'))).read()
            update_msg = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/update_attribute_msg.json'))).read()
            delete_msg = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/delete_attribute_msg.json'))).read()
            self.create_msg = json.loads(create_msg)
            self.update_msg = json.loads(update_msg)
            self.delete_msg = json.loads(delete_msg)
        except NameError as e:
            raise Exception('No Attribute Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        attribute = Attribute.from_json(self, self.create_msg)
        self.assertIsInstance(attribute, Attribute)
        self.assertTrue(hasattr(attribute, "id"))
        self.assertIs(attribute.id, 2)

if __name__ == '__main__':
   unittest.main()
