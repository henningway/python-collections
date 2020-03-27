import pytest

from fluent_collections import Fluent


@pytest.mark.parametrize("collection", [['foo', 'bar'], ('foo', 'bar')])
def test_first_returns_first_item(collection):
    c = Fluent(collection)
    assert 'foo' == c.first()


def test_first_returns_none_when_empty():
    c = Fluent()
    assert None is c.first()


@pytest.mark.parametrize("collection", [[], ()])
def test_empty_collection_is_empty(collection):
    c = Fluent(collection)
    assert c.is_empty()
