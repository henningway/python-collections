import pytest

from fluent_collections import Fluent


@pytest.mark.parametrize("collection", [['foo', 'bar'], ('foo', 'bar')])
def test_first_returns_first_item(collection):
    c = Fluent(collection)
    assert 'foo' == c.first()

    def test_empty_collection_is_empty(self):
        c = Fluent()
        self.assertTrue(c.is_empty())


@pytest.mark.parametrize("collection", [[], ()])
def test_empty_collection_is_empty(collection):
    c = Fluent(collection)
    assert c.is_empty()
