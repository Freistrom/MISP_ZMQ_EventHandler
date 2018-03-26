from sample.models.logo import Logo
import unittest
import json
import os


class LogoModelTest(unittest.TestCase):
    """User Model test cases."""

    def setUp(self):
        try:
            logo = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/models/logo.json')))
            self.logo = json.load(logo)
        except NameError as e:
            raise Exception('No Logo Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        logo = Logo.from_json(self, self.logo)
        self.assertIsInstance(logo, Logo)
        self.assertTrue(hasattr(logo, "name"))
        self.assertEqual(logo.name, 'test.png')
        self.assertTrue(hasattr(logo, "type"))
        self.assertEqual(logo.type, 'png')
        self.assertTrue(hasattr(logo, "tmp_name"))
        self.assertEqual(logo.tmp_name, 'test_802931578930587345793450.png')
        self.assertTrue(hasattr(logo, "error"))
        self.assertEqual(logo.error, 4)
        self.assertTrue(hasattr(logo, "size"))
        self.assertEqual(logo.size, 156)

    def test_to_json(self):
        logo = Logo.from_json(self, self.logo)
        self.assertDictEqual(logo.to_json(), self.logo)
