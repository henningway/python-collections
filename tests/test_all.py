import pytest

from fluent_collections import collect


@pytest.mark.parametrize("items", [['foo', 'bar'], ('foo', 'bar')])
def test_append_one(items):
    c = collect(items)
    assert type(items)(['foo', 'bar', 'baz']) == c.append('baz').eject()
    assert type(items)(['foo', 'bar']) == c.eject()  # immutable


@pytest.mark.parametrize("items", [['foo'], ('foo',)])
def test_append_multiple(items):
    c = collect(items)
    assert type(items)(['foo', 'bar', ['baz', 'qux']]) == c.append('bar', ['baz', 'qux']).eject()


@pytest.mark.parametrize("items", [[-666, 42, 0.1], (-666, 42, 0.1), {'a': -666, 'b': 42, 'c': 0.1}])
def test_avg(items):
    c = collect(items)
    assert -207.97 == round(c.avg(), 2)


@pytest.mark.parametrize("items", [['foo', 'bar'], ('foo', 'bar'), {'a': 'foo', 'b': 'bar'}])
def test_count(items):
    c = collect(items)
    assert 2 == c.count()


@pytest.mark.parametrize("items", [['foo', 'bar'], ('foo', 'bar'), {0: 'foo', 1: 'bar'}])
def test_eject(items):
    c = collect(items)
    assert items == c.eject()
    assert {0: 'foo', 1: 'bar'} == c.eject(dict)
    assert ['foo', 'bar'] == c.eject(list)
    assert ('foo', 'bar') == c.eject(tuple)


@pytest.mark.parametrize("items", [[2, 3, 1], (2, 3, 1), {'a': 2, 'b': 3, 'c': 1}])
def test_filter(items):
    c = collect(items)
    assert [2, 1] == c.filter(lambda v: v < 3).eject(list)
    assert [2, 3, 1] == c.eject(list)  # immutable


@pytest.mark.parametrize("items", [[2, 1, 0], (2, 1, 0), {0: 2, 1: 1, 2: 0}])
def test_filter_with_keys(items):
    c = collect(items)
    assert [2, 0] == c.filter(lambda v, k: k != v).eject(list)
    assert [2, 1, 0] == c.eject(list)  # immutable


@pytest.mark.parametrize("items", [['foo', 'bar'], ('foo', 'bar'), {'a': 'foo', 'b': 'bar'}])
def test_first_returns_first_item(items):
    c = collect(items)
    assert 'foo' == c.first()


def test_first_returns_none_when_empty():
    c = collect()
    assert None is c.first()


@pytest.mark.parametrize("items", [[], (), {}])
def test_empty_collection_is_empty(items):
    c = collect(items)
    assert c.is_empty()


@pytest.mark.parametrize("items", [[42], (42,), {'a': 42}])
def test_collection_is_not_empty(items):
    c = collect(items)
    assert not c.is_empty()


def test_keys():
    c = collect({'a': 'foo', 'b': 'bar'})
    assert ['a', 'b'] == c.keys()


@pytest.mark.parametrize("items", [['foo', 'bar'], ('foo', 'bar')])
def test_keys_non_dict(items):
    c = collect(items)
    assert [0, 1] == c.keys()


@pytest.mark.parametrize("items", [['foo', 'bar'], ('foo', 'bar'), {'a': 'foo', 'b': 'bar'}])
def test_last_returns_last_item(items):
    c = collect(items)
    assert 'bar' == c.last()


def test_last_returns_none_when_empty():
    c = collect()
    assert None is c.last()


@pytest.mark.parametrize("items", [['foo', 'bar'], ('foo', 'bar'), {'a': 'foo', 'b': 'bar'}])
def test_list(items):
    c = collect(items)
    assert ['foo', 'bar'] == c.eject(list)


@pytest.mark.parametrize("items", [['foo', 'bar'], ('foo', 'bar'), {'a': 'foo', 'b': 'bar'}])
def test_map(items):
    c = collect(items)
    assert ['oof', 'rab'] == c.map(lambda v: v[::-1]).eject(list)
    assert ['foo', 'bar'] == c.eject(list)  # immutable


@pytest.mark.parametrize("items", [[2, 1, 0], (2, 1, 0), {0: 2, 1: 1, 2: 0}])
def test_map_with_keys(items):
    c = collect(items)
    assert [2, 2, 2] == c.map(lambda v, k: k + v).eject(list)
    assert [2, 1, 0] == c.eject(list)  # immutable


@pytest.mark.parametrize("items", [[2, 1, 0], (2, 1, 0), {0: 2, 1: 1, 2: 0}])
def test_reduce(items):
    c = collect(items)
    assert 3 == c.reduce(lambda carry, value: carry + value)
    assert 6 == c.reduce(lambda carry, value: carry + value, 3)  # with initial value
    assert [2, 1, 0] == c.eject(list)  # immutable


@pytest.mark.parametrize("items", [[2, 1, 0], (2, 1, 0), {0: 2, 1: 1, 2: 0}])
def test_reduce_with_keys(items):
    c = collect(items)
    assert 6 == c.reduce(lambda x, y, k: x + y + k)
    assert [2, 1, 0] == c.eject(list)  # immutable


@pytest.mark.parametrize("items", [['foo', 'bar', 'baz'], ('foo', 'bar', 'baz'), {'a': 'foo', 'b': 'bar', 'c': 'baz'}])
def test_reverse(items):
    c = collect(items)
    assert ['baz', 'bar', 'foo'] == c.reverse().eject(list)
    assert ['foo', 'bar', 'baz'] == c.eject(list)  # immutable


@pytest.mark.parametrize("items", [
    [1, 2, 3, 4, 5, 6, 7],
    (1, 2, 3, 4, 5, 6, 7),
    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
])
def test_slice_start(items):
    c = collect(items)
    assert [4, 5, 6, 7] == c.slice(3).eject(list)


@pytest.mark.parametrize("items", [
    [1, 2, 3, 4, 5, 6, 7],
    (1, 2, 3, 4, 5, 6, 7),
    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
])
def test_slice_negative_start(items):
    c = collect(items)
    assert [5, 6, 7] == c.slice(-3).eject(list)


@pytest.mark.parametrize("items", [
    [1, 2, 3, 4, 5, 6, 7],
    (1, 2, 3, 4, 5, 6, 7),
    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
])
def test_slice_stop(items):
    c = collect(items)
    assert [3, 4, 5] == c.slice(2, 5).eject(list)


@pytest.mark.parametrize("items", [
    [1, 2, 3, 4, 5, 6, 7],
    (1, 2, 3, 4, 5, 6, 7),
    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
])
def test_slice_negative_stop(items):
    c = collect(items)
    assert [3, 4, 5] == c.slice(2, -2).eject(list)


@pytest.mark.parametrize("items", [
    [1, 2, 3, 4, 5, 6, 7],
    (1, 2, 3, 4, 5, 6, 7),
    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
])
def test_slice_negative_start_negative_stop(items):
    c = collect(items)
    assert [3, 4, 5] == c.slice(-5, -2).eject(list)


@pytest.mark.parametrize("items", [
    [1, 2, 3, 4, 5, 6, 7],
    (1, 2, 3, 4, 5, 6, 7),
    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
])
def test_slice_negative_start_positive_stop(items):
    c = collect(items)
    assert [4, 5, 6] == c.slice(-4, 6).eject(list)


@pytest.mark.parametrize("items", [
    [1, 2, 3, 4, 5, 6, 7],
    (1, 2, 3, 4, 5, 6, 7),
    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
])
def test_slice_step(items):
    c = collect(items)
    assert [3, 5] == c.slice(2, 6, 2).eject(list)


@pytest.mark.parametrize("items", [
    [1, 2, 3, 4, 5, 6, 7],
    (1, 2, 3, 4, 5, 6, 7),
    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
])
def test_slice_negative_start_stop_step(items):
    c = collect(items)
    assert [6, 4] == c.slice(-2, -5, -2).eject(list)


@pytest.mark.parametrize("items", [
    [1, 2, 3],
    (1, 2, 3),
    {'a': 1, 'b': 2, 'c': 3}
])
def test_slice_is_immutable(items):
    c = collect(items)
    assert [2, 3] == c.slice(1).eject(list)
    assert [1, 2, 3] == c.eject(list)  # immutable


@pytest.mark.parametrize("items", [[-666, 42, 0.1], (-666, 42, 0.1), {'a': -666, 'b': 42, 'c': 0.1}])
def test_sum(items):
    c = collect(items)
    assert -623.9 == c.sum()


@pytest.mark.parametrize("items", [['foo', 'bar', 'baz'], ('foo', 'bar', 'baz'), {'a': 'foo', 'b': 'bar', 'c': 'baz'}])
def test_take(items):
    c = collect(items)
    assert ['foo', 'bar'] == c.take(2).eject(list)
    assert ['foo', 'bar', 'baz'] == c.eject(list)  # immutable


@pytest.mark.parametrize("items", [['foo', 'bar', 'baz'], ('foo', 'bar', 'baz'), {'a': 'foo', 'b': 'bar', 'c': 'baz'}])
def test_take_last(items):
    c = collect(items)
    assert ['bar', 'baz'] == c.take(-2).eject(list)
    assert ['foo', 'bar', 'baz'] == c.eject(list)  # immutable
