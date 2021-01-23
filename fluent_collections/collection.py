from functools import reduce
from inspect import signature
from typing import Union, Tuple, List, Callable, Any, Optional, Dict


class Collection:
    _wrapped: Union[Dict, List, Tuple]

    def __init__(self, values=None):
        if values is None:
            values = []
        self._wrapped = values

    def all(self) -> Union[List, Tuple]:
        return self._wrapped

    # @TODO Dicts
    def append(self, *args) -> 'Collection':
        values = list(self._wrapped)

        for item in args:
            values.append(item)

        return Collection(type(self._wrapped)(values))

    def avg(self):
        """Returns the average of all items in the collection."""
        return self.sum() / self.count()

    def count(self) -> int:
        return len(self._wrapped)

    def dict(self) -> Dict:
        """
        Returns a Dict with all items in the collection. When the wrapped data structure is not a Dict the items are
        keyed via keys() with their zero-indexed position in the sequence.
        """

        if isinstance(self._wrapped, Dict):
            return self._wrapped

        return dict(zip(self.keys(), self.list()))

    def filter(self, f: Callable) -> 'Collection':
        """
        Returns a new collection of only those items in the collection that conform to the given predicate function f.
        f is expected to be able to look at each item individually and to make a statement about whether it should be in
        the new collection or not (return True or False or any equivalent value). If you want f to consider keys as well
        you should have it receive the key as second parameter. In case of Lists and Tuples, refer to keys() and dict()
        to learn how they are indexed.
        """

        if len(signature(f).parameters) > 1:
            filtered = filter(lambda x: f(x[1], x[0]), self.dict().items())
        else:
            filtered = filter(lambda x: f(x[1]), self.dict().items())

        if isinstance(self._wrapped, Dict):
            return Collection(dict(filtered))

        # note that for convenience we made it so that filtered always contains tuples of (key, value)
        return Collection(type(self._wrapped)([x[1] for x in filtered]))

    def first(self) -> Any:
        if not self._wrapped:
            return None

        if isinstance(self._wrapped, Dict):
            return list(self._wrapped.values())[0]

        return self._wrapped[0]

    def is_empty(self) -> bool:
        return not self._wrapped

    def keys(self) -> List:
        """
        Returns a List of all the keys in the collection. For Dicts this is straight-forward, but for other data
        structures this is essentially is a range with the length of the collection, starting at 0. This makes it easy
        to assign a zero-indexed-position to each item in the collection.
        """
        if isinstance(self._wrapped, Dict):
            return list(self._wrapped.keys())

        return list(range(self.count()))

    def last(self) -> Any:
        if not self._wrapped:
            return None

        if isinstance(self._wrapped, Dict):
            return list(self._wrapped.values())[-1]

        return self._wrapped[-1]

    def list(self) -> List:
        """
        Returns a List of all items in the collection. If the collection wraps a Dict this effectively removes the keys.
        """

        if isinstance(self._wrapped, Dict):
            return list(self._wrapped.values())

        return list(self._wrapped)

    def map(self, f: Callable) -> 'Collection':
        """
        Returns a new collection with every item transformed by the given function f. f should be able to handle the
        items in the collection and usually you want f to return some new (transformed) value. map() can be a convenient
        replacement for many for .. in loops or list comprehensions. If you want f to consider keys as well you should
        have it receive the key as second parameter. In case of Lists and Tuples, refer to keys() and dict() to learn
        how they are indexed.
        """

        if len(signature(f).parameters) > 1:
            mapped = map(f, self.list(), self.keys())
        else:
            mapped = map(f, self.list())

        if isinstance(self._wrapped, Dict):
            return Collection(dict(zip(self.keys(), mapped)))

        return Collection(type(self._wrapped)(mapped))

    # @TODO Dicts
    def reduce(self, f: Callable) -> Any:
        return reduce(f, self._wrapped)

    # @TODO Dicts
    def reverse(self):
        """Returns a new collection with the values in reversed order."""
        return Collection(self._wrapped[::-1])

    # @TODO supports Dicts, but gets the order wrong with negativ step, requires sort or reduce to be implemented first
    def slice(self, start: int, stop: Optional[int] = None, step: Optional[int] = None) -> 'Collection':
        """
        Slices the underlying data. Note that this method works a little different from Python builtin slices, to be a
        little more consistent as a function, without overloading. Builtin slices allow you to leave out start or stop,
        while here start has to be provided.
        """
        if isinstance(self._wrapped, Dict):
            sliced_keys = self.keys()[start:stop:step]
            return self.filter(lambda v, k: k in sliced_keys)

        return Collection(self._wrapped[start:stop:step])

    def sum(self):
        """Returns the sum of all items in the collection."""
        return sum(self.list())

    def take(self, limit: int) -> 'Collection':
        if limit < 0:
            return self.slice(limit)

        return self.slice(0, limit)


def collect(items=None):
    if items is None:
        return Collection([])
    return Collection(items)
