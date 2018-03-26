from sample.models.attribute import Attribute
import unittest
import json
import os


class AttributeModelTest(unittest.TestCase):
    """Event Model test cases."""

    def setUp(self):
        try:
            attribute = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/models/attribute.json')))
            self.attribute = json.load(attribute)
        except NameError as e:
            raise Exception('No Attribute Model Class defined!')

    def tearDown(self):
        pass

    def test_from_json(self):
        attribute = Attribute.from_json(self, self.attribute)
        self.assertIsInstance(attribute, Attribute)
        self.assertTrue(hasattr(attribute, "id"))
        self.assertEqual(attribute.id, 625)
        self.assertTrue(hasattr(attribute, "org_id"))
        self.assertIs(attribute.org_id, 1)
        self.assertTrue(hasattr(attribute, "date"))
        self.assertEqual(attribute.date, "2017-05-24")
        self.assertTrue(hasattr(attribute, "info"))
        self.assertEqual(attribute.info, "M2M - Fwd: IMG_3428.pdf")
        self.assertTrue(hasattr(attribute, "user_id"))
        self.assertEqual(attribute.user_id, 1)
        self.assertTrue(hasattr(attribute, "uuid"))
        self.assertEqual(attribute.uuid, "59259036-fcd0-4749-8a6c-4d88950d210f")
        self.assertTrue(hasattr(attribute, "published"))
        self.assertEqual(attribute.published, False)
        self.assertTrue(hasattr(attribute, "analysis"))
        self.assertEqual(attribute.analysis, 1)
        self.assertTrue(hasattr(attribute, "attribute_count"))
        self.assertEqual(attribute.attribute_count, 5)
        self.assertTrue(hasattr(attribute, "orgc_id"))
        self.assertEqual(attribute.orgc_id, 2)
        self.assertTrue(hasattr(attribute, "timestamp"))
        self.assertEqual(attribute.timestamp, "1505235275")
        self.assertTrue(hasattr(attribute, "distribution"))
        self.assertEqual(attribute.distribution, 3)
        self.assertTrue(hasattr(attribute, "sharing_group_id"))
        self.assertEqual(attribute.sharing_group_id, 0)
        self.assertTrue(hasattr(attribute, "proposal_email_lock"))
        self.assertEqual(attribute.proposal_email_lock, False)
        self.assertTrue(hasattr(attribute, "locked"))
        self.assertEqual(attribute.locked, False)
        self.assertTrue(hasattr(attribute, "threat_level_id"))
        self.assertEqual(attribute.threat_level_id, 3)
        self.assertTrue(hasattr(attribute, "publish_timestamp"))
        self.assertEqual(attribute.publish_timestamp, "1505233367")
        self.assertTrue(hasattr(attribute, "disable_correlation"))
        self.assertEqual(attribute.disable_correlation, False)

    def test_to_json(self):
        attribute = Attribute.from_json(self, self.attribute)
        self.assertDictEqual(attribute.to_json(), self.attribute)
