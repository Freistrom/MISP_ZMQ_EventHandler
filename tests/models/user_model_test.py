from sample.models.user import User
import unittest
import json
import os


class UserModelTest(unittest.TestCase):
    """User Model test cases."""

    @classmethod
    def setupClass(cls):
        try:
            user = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/models/user.json')))
            cls.user = json.load(user)
        except NameError as e:
            raise Exception('No User Model Class defined!')

    @classmethod
    def teardownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass  # clean up

    def test_from_json(self):
        user = User.from_json(self, self.user)
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, "id"))
        self.assertEqual(user.id, 4)
        self.assertTrue(hasattr(user, "server_id"))
        self.assertEqual(user.server_id, 0)
        self.assertTrue(hasattr(user, "autoalert"))
        self.assertEqual(user.autoalert, 1)
        self.assertTrue(hasattr(user, "nids_sid"))
        self.assertEqual(user.nids_sid, 5976699)
        self.assertTrue(hasattr(user, "termsaccepted"))
        self.assertEqual(user.termsaccepted, 0)
        self.assertTrue(hasattr(user, "role_id"))
        self.assertEqual(user.role_id, 3)
        self.assertTrue(hasattr(user, "change_pw"))
        self.assertEqual(user.change_pw, 1)
        self.assertTrue(hasattr(user, "contactalert"))
        self.assertEqual(user.contactalert, 1)
        self.assertTrue(hasattr(user, "disabled"))
        self.assertEqual(user.disabled, 0)
        self.assertTrue(hasattr(user, "current_login"))
        self.assertEqual(user.current_login, 0)
        self.assertTrue(hasattr(user, "last_login"))
        self.assertEqual(user.last_login, 0)
        self.assertTrue(hasattr(user, "force_logout"))
        self.assertEqual(user.force_logout, 0)
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "user@testemail.com")
        self.assertTrue(hasattr(user, "enable_password"))
        self.assertEqual(user.enable_password, 0)
        self.assertTrue(hasattr(user, "org_id"))
        self.assertEqual(user.org_id, 1)
        self.assertTrue(hasattr(user, "authkey"))
        self.assertEqual(user.authkey, "__<redacted>__")
        self.assertTrue(hasattr(user, "gpgkey"))
        self.assertEqual(user.gpgkey, "__<redacted>__")
        self.assertTrue(hasattr(user, "notify"))
        self.assertEqual(user.notify, 1)
        self.assertTrue(hasattr(user, "date_created"))
        self.assertEqual(user.date_created, "1000000000")
        self.assertTrue(hasattr(user, "date_modified"))
        self.assertEqual(user.date_modified, "1000000000")
        self.assertTrue(hasattr(user, "newsread"))
        self.assertEqual(user.newsread, 0)
        self.assertTrue(hasattr(user, "certif_public"))
        self.assertEqual(user.certif_public, "")

    def test_to_json(self):
        user = User.from_json(self, self.user)
        self.assertDictEqual(user.to_json(), self.user)
