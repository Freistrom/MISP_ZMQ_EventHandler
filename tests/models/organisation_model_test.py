from sample.models.organisation import Organisation
import unittest
import json
import os
import pdb


class OrganisationModelTest(unittest.TestCase):
    """Organisation Model test cases."""

    def setUp(self):
        try:
            organisation = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/organisation.json')))
            self.organisation = json.load(organisation)
        except NameError as e:
            raise Exception('No Organisation Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        organisation = Organisation.from_json(self, self.organisation)
        self.assertIsInstance(organisation, Organisation)
        self.assertTrue(hasattr(organisation, "id"))
        self.assertIs(organisation.id, 10)

if __name__ == '__main__':
   unittest.main()
