import pytest

from fluent_collections import Fluent


@pytest.mark.parametrize("collection", [[], ()])
def test_empty_collection_is_empty(collection):
    c = Fluent(collection)
    assert c.is_empty()


@pytest.mark.parametrize("collection", [['foo', 'bar'], ('foo', 'bar')])
def test_count(collection):
    c = Fluent(collection)
    assert 2 == c.count()


@pytest.mark.parametrize("collection", [['foo', 'bar'], ('foo', 'bar')])
def test_all_returns_wrapped_collection(collection):
    c = Fluent(collection)
    assert c.all() == collection


@pytest.mark.parametrize("collection", [['foo', 'bar'], ('foo', 'bar')])
def test_first_returns_first_item(collection):
    c = Fluent(collection)
    assert 'foo' == c.first()


def test_first_returns_none_when_empty():
    c = Fluent()
    assert None is c.first()


@pytest.mark.parametrize("collection", [['foo', 'bar'], ('foo', 'bar')])
def test_last_returns_last_item(collection):
    c = Fluent(collection)
    assert 'bar' == c.last()


def test_last_returns_none_when_empty():
    c = Fluent()
    assert None is c.last()


@pytest.mark.parametrize("collection", [['foo', 'bar'], ('foo', 'bar')])
def test_map(collection):
    c = Fluent(collection)
    assert type(collection)(['oof', 'rab']) == c.map(lambda s: s[::-1])


@pytest.mark.parametrize("collection", [[2, 3, 1], (2, 3, 1)])
def test_filter(collection):
    c = Fluent(collection)
    assert type(collection)([2, 1]) == c.filter(lambda x: x < 3)
