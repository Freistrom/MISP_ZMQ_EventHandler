from sample.models.logo import Logo
import unittest
import json
import os

class LogoModelTest(unittest.TestCase):
    """User Model test cases."""

    def setUp(self):
        try:
            logo = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/logo.json')))
            self.logo = json.load(logo)
        except NameError as e:
            raise Exception('No Logo Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        logo = Logo.from_json(self, self.logo)
        self.assertIsInstance(logo, Logo)
        #self.assertTrue(hasattr(logo, "id"))
        #self.assertIs(logo.id, 2)

if __name__ == '__main__':
   unittest.main()
