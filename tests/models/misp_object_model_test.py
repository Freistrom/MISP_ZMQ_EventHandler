from sample.models.misp_object import MispObject
import unittest
import json
import os

class MispObjectModelTest(unittest.TestCase):
    """Event Model test cases."""

    def setUp(self):
        try:
            msg = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/misp_object_msg.json'))).read()
            self.msg = json.loads(msg)
        except NameError as e:
            raise Exception('No MispObject Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        misp_object = MispObject.from_json(self, self.msg)
        self.assertIsInstance(misp_object, MispObject)
        self.assertTrue(hasattr(misp_object, "id"))
        self.assertIs(misp_object.id, 2)

if __name__ == '__main__':
   unittest.main()
