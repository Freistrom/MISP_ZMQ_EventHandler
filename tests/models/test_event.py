from .context import sample
import unittest

class EventModelTestSuite(unittest.TestCase):
    """Event Model test cases."""

    def test_by_json(self):
        self.assertIsNone(models.Event.by_json('"Event":{}'))


if __name__ == '__main__':
	unittest.main()