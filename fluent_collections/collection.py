from functools import reduce
from inspect import signature
from typing import Union, Tuple, List, Callable, Any, Optional, Dict, Type


class Collection:
    _wrapped: Union[Dict, List, Tuple]

    def __init__(self, values=None):
        if values is None:
            values = []
        self._wrapped = values

    # @TODO support dict
    def append(self, *args) -> 'Collection':
        values = list(self._wrapped)

        for item in args:
            values.append(item)

        return Collection(type(self._wrapped)(values))

    def avg(self):
        """Returns the average of all items in the collection."""
        return self.sum() / self.count()

    # @TODO docstring
    def count(self) -> int:
        return len(self._wrapped)

    def eject(self, target: Union[Type[dict], Type[list], Type[tuple]] = None):
        """
        Returns all items in the collection in the original native python compound data type (dict, list ,tuple). You
        can specify an optional target type to have the result be casted to that type.

        When you are casting from a wrapped list or tuple to a dict, the items are keyed via keys() with their
        zero-indexed position previously to ejection. Conversely, when you are casting from a wrapped dict to list or
        tuple, this effectively removes the keys.
        """
        if target is not None:
            assert target in [dict, list, tuple], f"Unknown target type {target}. Allowed values: dict, list, tuple."

        if target is None or isinstance(self._wrapped, target):
            return self._wrapped

        if target in [list, tuple]:
            return target(self._wrapped.values()) if isinstance(self._wrapped, dict) else target(self._wrapped)

        if target == dict:
            if isinstance(self._wrapped, dict):
                return self._wrapped

            return dict(zip(self.keys(), self.eject(list)))

        raise TypeError(f"Can't eject {type(self._wrapped)} with target type {target}.")

    def filter(self, f: Callable) -> 'Collection':
        """
        Returns a new collection of only those items in the collection that conform to the given predicate function f.
        f is expected to be able to look at each item individually and to make a statement about whether it should be in
        the new collection or not (return True or False or any equivalent value).

        If you want f to consider keys as well you should have it receive the key as second parameter. In case of lists
        and tuples, refer to keys() and eject(dict) to learn how they are indexed.
        """

        parameter_count = len(signature(f).parameters)

        assert parameter_count in [1, 2], \
            f"Filter function should accept one (values) or two arguments (+ keys), but the arity is {parameter_count}."

        if parameter_count == 2:
            filtered = filter(lambda x: f(x[1], x[0]), self.eject(dict).items())
        else:
            filtered = filter(lambda x: f(x[1]), self.eject(dict).items())

        if isinstance(self._wrapped, dict):
            return Collection(dict(filtered))

        # Note that to keep the implementation simple `filtered` always contains tuples of (key, value) which is why we
        # have to throw away the keys unless we want to return a dict. To optimize this, we could stop carrying along
        # the keys when not absolutely required.
        return Collection(type(self._wrapped)([x[1] for x in filtered]))

    def first(self) -> Any:
        if not self._wrapped:
            return None

        if isinstance(self._wrapped, dict):
            return list(self._wrapped.values())[0]

        return self._wrapped[0]

    def is_empty(self) -> bool:
        return not self._wrapped

    # @TODO test, docstring
    def into(self, target: Union[Type[dict], Type[list], Type[tuple]]) -> 'Collection':
        return Collection(self.eject(target))

    def keys(self) -> List:
        """
        Returns a List of all the keys in the collection. For Dicts this is straight-forward, but for other data
        structures this is essentially is a range with the length of the collection, starting at 0. This makes it easy
        to assign a zero-indexed-position to each item in the collection.
        """
        if isinstance(self._wrapped, dict):
            return list(self._wrapped.keys())

        return list(range(self.count()))

    # @TODO docstring
    def last(self) -> Any:
        if not self._wrapped:
            return None

        if isinstance(self._wrapped, dict):
            return list(self._wrapped.values())[-1]

        return self._wrapped[-1]

    def map(self, f: Callable) -> 'Collection':
        """
        Returns a new collection with every item transformed by the given function f. f should be able to handle the
        items in the collection and usually you want f to return some new (transformed) value. map() can be a convenient
        replacement for many for .. in loops or list comprehensions. If you want f to consider keys as well you should
        have it receive the key as second parameter. In case of Lists and Tuples, refer to keys() and eject(dict) to learn
        how they are indexed.
        """

        parameter_count = len(signature(f).parameters)

        assert parameter_count in [1, 2], \
            f"Filter function should accept one (value) or two arguments (value, key), but the arity is {parameter_count}."

        if parameter_count == 1:
            mapped = map(f, self.eject(list))
        else:
            mapped = map(f, self.eject(list), self.keys())

        if isinstance(self._wrapped, dict):
            return Collection(dict(zip(self.keys(), mapped)))

        return Collection(type(self._wrapped)(mapped))

    # @TODO test for edge cases: empty collection, one value in either initial or collection
    def reduce(self, f: Callable, initial: Any = None) -> Any:
        """
        Returns the result of applying f to the first two values in the collection, then to the resulting value and the
        next value in the collection and so on.
        """

        parameter_count = len(signature(f).parameters)

        assert parameter_count in [2, 3], \
            f"Reducing function should accept two (carry, value) or three arguments (carry, value, key), but the arity is {parameter_count}."
        assert initial is not None or self.count() > 0, \
            "Cannot reduce empty collection without initial value."

        g = (
            lambda carry, item: f(carry, item[1]),  # only value of item provided to reducing function, key ignored
            lambda carry, item: f(carry, item[1], item[0])  # key of next value supported as third argument
        )[parameter_count - 2]

        rest = self.into(dict)

        if initial is None:
            (initial, rest) = (self.first(), rest.rest())

        return reduce(g, rest.eject().items(), initial)

    # @TODO test
    def rest(self):
        """Returns a new collection that contains all values except the first."""
        return self.slice(1)

    # @TODO dict support will work as soon as slice supports negative indices with Dicts
    def reverse(self):
        """Returns a new collection with the values in reversed order."""
        return self.slice(-1, None, -1)

    # @TODO supports dicts, but gets the order wrong with negative step, requires sort or reduce to be implemented first
    def slice(self, start: int, stop: Optional[int] = None, step: Optional[int] = None) -> 'Collection':
        """
        Slices the underlying data. Note that this method works a little different from Python builtin slices, to be a
        little more consistent as a function, without overloading. Builtin slices allow you to leave out start or stop,
        while here start has to be provided.
        """
        if isinstance(self._wrapped, dict):
            sliced_keys = self.keys()[start:stop:step]
            return self.filter(lambda v, k: k in sliced_keys)

        return Collection(self._wrapped[start:stop:step])

    # @TODO docstring
    def sum(self):
        """Returns the sum of all items in the collection."""
        return sum(self.eject(list))

    # @TODO docstring
    def take(self, limit: int) -> 'Collection':
        if limit < 0:
            return self.slice(limit)

        return self.slice(0, limit)


def collect(items=None):
    if items is None:
        return Collection([])
    return Collection(items)
