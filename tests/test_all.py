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


@pytest.mark.parametrize("items", [[1, 2, 3, 4, 5, 6, 7], (1, 2, 3, 4, 5, 6, 7)])
def test_slice_start(items):
    c = collect(items)
    assert type(items)([4, 5, 6, 7]) == c.slice(3).all()


@pytest.mark.parametrize("items", [[1, 2, 3, 4, 5, 6, 7], (1, 2, 3, 4, 5, 6, 7)])
def test_slice_negative_start(items):
    c = collect(items)
    assert type(items)([5, 6, 7]) == c.slice(-3).all()


@pytest.mark.parametrize("items", [[1, 2, 3, 4, 5, 6, 7], (1, 2, 3, 4, 5, 6, 7)])
def test_slice_stop(items):
    c = collect(items)
    assert type(items)([3, 4, 5]) == c.slice(2, 5).all()


@pytest.mark.parametrize("items", [[1, 2, 3, 4, 5, 6, 7], (1, 2, 3, 4, 5, 6, 7)])
def test_slice_negative_stop(items):
    c = collect(items)
    assert type(items)([3, 4, 5]) == c.slice(2, -2).all()


@pytest.mark.parametrize("items", [[1, 2, 3, 4, 5, 6, 7], (1, 2, 3, 4, 5, 6, 7)])
def test_slice_negative_start_negative_stop(items):
    c = collect(items)
    assert type(items)([3, 4, 5]), c.slice(-5, -2).all()


@pytest.mark.parametrize("items", [[1, 2, 3, 4, 5, 6, 7], (1, 2, 3, 4, 5, 6, 7)])
def test_slice_negative_start_positive_stop(items):
    c = collect(items)
    assert type(items)([4, 5, 6]) == c.slice(-4, 6).all()


@pytest.mark.parametrize("items", [[1, 2, 3, 4, 5, 6, 7], (1, 2, 3, 4, 5, 6, 7)])
def test_slice_step(items):
    c = collect(items)
    assert type(items)([3, 5]) == c.slice(2, 6, 2).all()


@pytest.mark.parametrize("items", [[1, 2, 3, 4, 5, 6, 7], (1, 2, 3, 4, 5, 6, 7)])
def test_slice_negative_start_stop_step(items):
    c = collect(items)
    assert type(items)([6, 4]) == c.slice(-2, -5, -2).all()


@pytest.mark.parametrize("items", [['foo', 'bar', 'baz'], ('foo', 'bar', 'baz')])
def test_take(items):
    c = collect(items)
    assert type(items)(['foo', 'bar']) == c.take(2).all()


@pytest.mark.parametrize("items", [['foo', 'bar', 'baz'], ('foo', 'bar', 'baz')])
def test_take_last(items):
    c = collect(items)
    assert type(items)(['bar', 'baz']) == c.take(-2).all()


@pytest.mark.parametrize("items", [['foo', 'bar'], ('foo', 'bar')])
def test_append_one(items):
    c = collect(items)
    assert type(items)(['foo', 'bar', 'baz']) == c.append('baz').all()


@pytest.mark.parametrize("items", [['foo'], ('foo',)])
def test_append_multiple(items):
    c = collect(items)
    assert type(items)(['foo', 'bar', ['baz', 'qux']]) == c.append('bar', ['baz', 'qux']).all()


@pytest.mark.parametrize("items", [[-666, 42, 0.1], (-666, 42, 0.1)])
def test_sum(items):
    c = collect(items)
    assert -623.9 == c.sum()
