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

    def filter(self, callback: Callable) -> 'Collection':
        filtered = filter(callback, self._wrapped)

        if isinstance(self._wrapped, Tuple):
            return Collection(tuple(filtered))

        return Collection(list(filtered))

    def first(self) -> Any:
        if not self._wrapped:
            return None

        if isinstance(self._wrapped, Dict):
            return list(self._wrapped.values())[0]

        return self._wrapped[0]

    def is_empty(self) -> bool:
        return not self._wrapped

    def keys(self) -> List:
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
        """Returns a list of all items in the collection."""

        if isinstance(self._wrapped, Dict):
            return list(self._wrapped.values())

        return list(self._wrapped)

    def map(self, callback: Callable) -> 'Collection':
        if len(signature(callback).parameters) > 1:
            mapped = map(callback, self.list(), self.keys())
        else:
            mapped = map(callback, self.list())

        if isinstance(self._wrapped, Dict):
            return Collection(dict(zip(self.keys(), mapped)))

        return Collection(type(self._wrapped)(mapped))

    def reduce(self, callback: Callable) -> Any:
        return reduce(callback, self._wrapped)

    def reverse(self):
        """Returns a new collection with the values in reversed order."""
        return Collection(self._wrapped[::-1])

    def slice(self, start: int, stop: Optional[int] = None, step: Optional[int] = None) -> 'Collection':
        """
        Slices the underlying data. Note that this method works a little different from Python builtin slices, to be a
        little more consistent as a function, without overloading. Builtin slices allow you to leave out start or stop,
        while here start has to be provided.
        """
        return Collection(self._wrapped[start:stop:step])

    def sum(self):
        """Returns the sum of all items in the collection."""
        return sum(self._wrapped)

    def take(self, limit: int) -> 'Collection':
        if limit < 0:
            return self.slice(limit)

        return self.slice(0, limit)


def collect(items=None):
    if items is None:
        return Collection([])
    return Collection(items)
