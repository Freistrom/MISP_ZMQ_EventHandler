from sample.models.organisation import Organisation
import unittest
import json
import os

class OrganisationModelTest(unittest.TestCase):
    """Event Model test cases."""

    def setUp(self):
        try:
            create_msg = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/create_organisation_msg.json'))).read()
            update_msg = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/update_organisation_msg.json'))).read()
            self.create_msg = json.loads(create_msg)
            self.update_msg = json.loads(update_msg)
        except NameError as e:
            raise Exception('No Organisation Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        organisation = Organisation.from_json(self, self.create_msg)
        self.assertIsInstance(organisation, Organisation)
        self.assertTrue(hasattr(organisation, "id"))
        self.assertIs(organisation.id, 2)

if __name__ == '__main__':
   unittest.main()
