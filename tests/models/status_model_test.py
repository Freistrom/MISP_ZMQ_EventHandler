from sample.models.status import Status
import unittest
import json
import os

class StatusModelTest(unittest.TestCase):
    """Status Model test cases."""

    def setUp(self):
        try:
            status = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/status.json')))
            self.status = json.load(status)
        except NameError as e:
            raise Exception('No Status Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        status = Status.from_json(self, self.status)
        self.assertIsInstance(status, Status)
        #self.assertTrue(hasattr(status, "id"))
        #self.assertIs(status.id, 2)

if __name__ == '__main__':
   unittest.main()
