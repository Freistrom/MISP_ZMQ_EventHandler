from sample.models.message import Message
import unittest
import json
import os

class MessageModelTest(unittest.TestCase):
    """Event Model test cases."""

    def setUp(self):
        try:
            msg = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/message_msg.json'))).read()
            self.msg = json.loads(msg)
        except NameError as e:
            raise Exception('No Message Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        message = Message.from_json(self, self.msg)
        self.assertIsInstance(message, Message)
        self.assertTrue(hasattr(message, "id"))
        self.assertIs(message.id, 2)

if __name__ == '__main__':
   unittest.main()
