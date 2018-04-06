from src.models.sighting import Sighting
import unittest
import json
import os


class SightingModelTest(unittest.TestCase):
    """Sighting Model test cases."""

    @classmethod
    def setupClass(cls):
        try:
            sighting = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/models/sighting.json')))
            cls.sighting = json.load(sighting)
        except NameError as e:
            raise Exception('No Sighting Model Class defined!')

    @classmethod
    def teardownClass(cls):
        pass

    def setUp(self):
        try:
            sighting = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/models/sighting.json')))
            self.sighting = json.load(sighting)
        except NameError as e:
            raise Exception('No Sighting Model Class defined!')

    def tearDown(self):
        pass  # clean up

    def test_from_json(self):
        sighting = Sighting.from_json(self, self.sighting)
        self.assertIsInstance(sighting, Sighting)
        self.assertTrue(hasattr(sighting, "id"))
        self.assertEqual(sighting.id, 1)
        self.assertTrue(hasattr(sighting, "attribute_id"))
        self.assertEqual(sighting.attribute_id, 164373)
        self.assertTrue(hasattr(sighting, "event_id"))
        self.assertEqual(sighting.event_id, 625)
        self.assertTrue(hasattr(sighting, "org_id"))
        self.assertEqual(sighting.org_id, 1)
        self.assertTrue(hasattr(sighting, "date_sighting"))
        self.assertEqual(sighting.date_sighting, "1505767537")
        self.assertTrue(hasattr(sighting, "source"))
        self.assertEqual(sighting.source, "")
        self.assertTrue(hasattr(sighting, "uuid"))
        self.assertEqual(sighting.uuid, "59c03071-f480-4311-a710-03edc0a83832")

    def test_to_json(self):
        sighting = Sighting.from_json(self, self.sighting)
        self.assertDictEqual(sighting.to_json(), self.sighting)
