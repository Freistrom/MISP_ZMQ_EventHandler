from sample.models.status import Status
import unittest
import json
import os

class StatusModelTest(unittest.TestCase):
    """Event Model test cases."""

    def setUp(self):
        try:
            msg = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/status_msg.json'))).read()
            self.msg = json.loads(msg)
        except NameError as e:
            raise Exception('No Status Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        status = Status.from_json(self, self.msg)
        self.assertIsInstance(status, Status)
        self.assertTrue(hasattr(status, "id"))
        self.assertIs(status.id, 2)

if __name__ == '__main__':
   unittest.main()
