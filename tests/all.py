import unittest

from fluent_collections import Fluent


class AllTests(unittest.TestCase):
    def test_first_returns_first_item(self):
        c = Fluent(['foo', 'bar'])
        self.assertEqual('foo', c.first())

    def test_empty_collection_is_empty(self):
        c = Fluent()
        self.assertTrue(c.is_empty())


if __name__ == '__main__':
    unittest.main()
