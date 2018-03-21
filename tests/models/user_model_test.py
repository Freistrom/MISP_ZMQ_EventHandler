from sample.models.user import User
import unittest
import json
import os

class UserModelTest(unittest.TestCase):
    """Event Model test cases."""

    def setUp(self):
        try:
            login_msg = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/login_user_msg.json'))).read()
            create_msg = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/create_user_msg.json'))).read()
            self.login_msg = json.loads(login_msg)
            self.create_msg = json.loads(create_msg)
        except NameError as e:
            raise Exception('No User Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        user = User.from_json(self, self.login_msg)
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, "id"))
        self.assertIs(user.id, 2)

if __name__ == '__main__':
   unittest.main()
