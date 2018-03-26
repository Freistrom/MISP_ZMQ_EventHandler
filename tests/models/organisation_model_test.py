import unittest
import json
import os
from sample.models.organisation import Organisation
from sample.models.logo import Logo


class OrganisationModelTest(unittest.TestCase):
    """Organisation Model test cases."""

    def setUp(self):
        try:
            organisation = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/models/organisation.json')))
            self.organisation = json.load(organisation)
        except NameError as e:
            raise Exception('No Organisation Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        organisation = Organisation.from_json(self, self.organisation)
        self.assertIsInstance(organisation, Organisation)
        self.assertTrue(hasattr(organisation, "id"))
        self.assertEqual(organisation.id, 10)
        self.assertTrue(hasattr(organisation, "local"))
        self.assertEqual(organisation.local, 1)
        self.assertTrue(hasattr(organisation, "name"))
        self.assertEqual(organisation.name, "test")
        self.assertTrue(hasattr(organisation, "uuid"))
        self.assertEqual(organisation.uuid, "59c0367d-fe8c-42a4-9db2-03ecc0a83832")
        self.assertTrue(hasattr(organisation, "description"))
        self.assertEqual(organisation.description, "Alternate Test")
        self.assertTrue(hasattr(organisation, "nationality"))
        self.assertEqual(organisation.nationality, "Not specified")
        self.assertTrue(hasattr(organisation, "sector"))
        self.assertEqual(organisation.sector, "")
        self.assertTrue(hasattr(organisation, "type"))
        self.assertEqual(organisation.type, "")
        self.assertTrue(hasattr(organisation, "contacts"))
        self.assertEqual(organisation.contacts, "")
        self.assertTrue(hasattr(organisation, "date_modified"))
        self.assertEqual(organisation.date_modified, "2017-09-18 23:11:37")
        self.assertTrue(hasattr(organisation, "logo"))
        self.assertIsInstance(organisation.logo, Logo)
        self.assertTrue(hasattr(organisation.logo, "name"))
        self.assertEqual(organisation.logo.name, "test.png")
        self.assertTrue(hasattr(organisation.logo, "type"))
        self.assertEqual(organisation.logo.type, "png")
        self.assertTrue(hasattr(organisation.logo, "tmp_name"))
        self.assertEqual(organisation.logo.tmp_name, "test_0943857394557.png")
        self.assertTrue(hasattr(organisation.logo, "error"))
        self.assertEqual(organisation.logo.error, 4)
        self.assertTrue(hasattr(organisation.logo, "size"))
        self.assertEqual(organisation.logo.size, 544)

    def test_to_json(self):
        organisation = Organisation.from_json(self, self.organisation)
        self.assertDictEqual(organisation.to_json(), self.organisation)
