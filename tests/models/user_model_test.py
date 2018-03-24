from sample.models.user import User
import unittest
import json
import os

class UserModelTest(unittest.TestCase):
    """User Model test cases."""

    def setUp(self):
        try:
            user = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/user.json')))
            self.user = json.load(user)
        except NameError as e:
            raise Exception('No User Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        user = User.from_json(self, self.user)
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, "id"))
        self.assertIs(user.id, 4)

if __name__ == '__main__':
   unittest.main()
