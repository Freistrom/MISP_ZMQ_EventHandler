from sample.models.tag import Tag
import unittest
import json
import os


class TagModelTest(unittest.TestCase):
    """Tag Model test cases."""

    def setUp(self):
        try:
            tag = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/models/tag.json')))
            self.tag = json.load(tag)
        except NameError as e:
            raise Exception('No Tag Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_by_json(self):
        tag = Tag.from_json(self, self.tag)
        self.assertIsInstance(tag, Tag)
        self.assertTrue(hasattr(tag, "id"))
        self.assertEqual(tag.id, 1)
        self.assertTrue(hasattr(tag, "name"))
        self.assertEqual(tag.name, "dfdgddddd")
        self.assertTrue(hasattr(tag, "colour"))
        self.assertEqual(tag.colour, "#c40808")
        self.assertTrue(hasattr(tag, "exportable"))
        self.assertEqual(tag.exportable, 1)
        self.assertTrue(hasattr(tag, "org_id"))
        self.assertEqual(tag.org_id, 1)
        self.assertTrue(hasattr(tag, "user_id"))
        self.assertEqual(tag.user_id, 2)
        self.assertTrue(hasattr(tag, "hide_tag"))
        self.assertEqual(tag.hide_tag, 0)

    def test_to_json(self):
        tag = Tag.from_json(self, self.tag)
        self.assertDictEqual(tag.to_json(), self.tag)
