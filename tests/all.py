import unittest

from threadable import Threadable


class AllTests(unittest.TestCase):
    def test_first_returns_first_item(self):
        c = Threadable(['foo', 'bar'])
        self.assertEqual('foo', c.first())


if __name__ == '__main__':
    unittest.main()
