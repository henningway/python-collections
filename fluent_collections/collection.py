from functools import reduce
from typing import Union, Tuple, List, Callable, Any, Optional


class Collection:
    _values: Union[List, Tuple]

    def __init__(self, values=None):
        if values is None:
            values = []
        self._values = values

    def all(self) -> Union[List, Tuple]:
        return self._values

    def count(self) -> int:
        return len(self._values)

    def filter(self, callback: Callable) -> 'Collection':
        filtered = filter(callback, self._values)

        if isinstance(self._values, Tuple):
            return Collection(tuple(filtered))

        return Collection(list(filtered))

    def first(self) -> Any:
        if not self._values:
            return None

        return self._values[0]

    def is_empty(self) -> bool:
        return not self._values

    def last(self) -> Any:
        if not self._values:
            return None

        return self._values[-1]

    def map(self, callback: Callable) -> 'Collection':
        mapped = map(callback, self._values)

        if isinstance(self._values, Tuple):
            return Collection(tuple(mapped))

        return Collection(list(mapped))

    def reduce(self, callback: Callable) -> Any:
        return reduce(callback, self._values)

    def slice(self, start: int, stop: Optional[int] = None, step: Optional[int] = None) -> 'Collection':
        """
        Slices the underlying data. Note that this method works a little different from Python builtin slices, to be a
        little more consistent as a function, without overloading. Builtin slices allow you to leave out start or stop,
        while here start has to be provided.
        """
        return Collection(self._values[start:stop:step])


def collect(items=None):
    if items is None:
        return Collection([])
    return Collection(items)
