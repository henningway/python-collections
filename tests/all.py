import unittest

from threadable import Threadable


class AllTests(unittest.TestCase):
    def test_first_returns_first_item(self):
        c = Threadable(['foo', 'bar'])
        self.assertEqual('foo', c.first())

    def test_empty_collection_is_empty(self):
        c = Threadable()
        self.assertTrue(c.is_empty())


if __name__ == '__main__':
    unittest.main()
