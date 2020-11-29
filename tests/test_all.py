import pytest

from fluent_collections import collect


@pytest.mark.parametrize("items", [[], ()])
def test_empty_collection_is_empty(items):
    c = collect(items)
    assert c.is_empty()


@pytest.mark.parametrize("items", [['foo', 'bar'], ('foo', 'bar')])
def test_count(items):
    c = collect(items)
    assert 2 == c.count()


@pytest.mark.parametrize("items", [['foo', 'bar'], ('foo', 'bar')])
def test_all_returns_wrapped_items(items):
    c = collect(items)
    assert c.all() == items


@pytest.mark.parametrize("items", [['foo', 'bar'], ('foo', 'bar')])
def test_first_returns_first_item(items):
    c = collect(items)
    assert 'foo' == c.first()


def test_first_returns_none_when_empty():
    c = collect()
    assert None is c.first()


@pytest.mark.parametrize("items", [['foo', 'bar'], ('foo', 'bar')])
def test_last_returns_last_item(items):
    c = collect(items)
    assert 'bar' == c.last()


def test_last_returns_none_when_empty():
    c = collect()
    assert None is c.last()


@pytest.mark.parametrize("items", [['foo', 'bar'], ('foo', 'bar')])
def test_map(items):
    c = collect(items)
    assert type(items)(['oof', 'rab']) == c.map(lambda s: s[::-1]).all()


@pytest.mark.parametrize("items", [[2, 3, 1], (2, 3, 1)])
def test_filter(items):
    c = collect(items)
    assert type(items)([2, 1]) == c.filter(lambda x: x < 3).all()


@pytest.mark.parametrize("items", [[1, 2, 3], (1, 2, 3)])
def test_reduce(items):
    c = collect(items)
    assert 6 == c.reduce(lambda x, y: x + y)
