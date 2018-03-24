from sample.models.tag import Tag
import unittest
import json
import os

class TagModelTest(unittest.TestCase):
    """Tag Model test cases."""

    def setUp(self):
        try:
            tag = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/tag.json')))
            self.tag = json.load(tag)
        except NameError as e:
            raise Exception('No Tag Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        tag = Tag.from_json(self, self.tag)
        self.assertIsInstance(tag, Tag)
        self.assertTrue(hasattr(tag, "id"))
        self.assertIs(tag.id, 1)

if __name__ == '__main__':
   unittest.main()
