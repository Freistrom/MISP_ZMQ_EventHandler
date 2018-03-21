from sample.models.galaxy import Galaxy
import unittest
import json
import os

class GalaxyModelTest(unittest.TestCase):
    """Event Model test cases."""

    def setUp(self):
        try:
            msg = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/galaxy_msg.json'))).read()
            self.msg = json.loads(msg)
        except NameError as e:
            raise Exception('No Galaxy Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        galaxy = Galaxy.from_json(self, self.msg)
        self.assertIsInstance(galaxy, Galaxy)
        self.assertTrue(hasattr(galaxy, "id"))
        self.assertIs(galaxy.id, 2)

if __name__ == '__main__':
   unittest.main()
