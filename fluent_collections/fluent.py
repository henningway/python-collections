from typing import Union, Tuple, List, Callable, Any

Collection = Union[List, Tuple]


class Fluent:
    _values: Collection

    def __init__(self, values=None):
        if values is None:
            values = []
        self._values = values

    def is_empty(self) -> bool:
        return not self._values

    def count(self) -> int:
        return len(self._values)

    def all(self) -> Collection:
        return self._values

    def first(self) -> Any:
        if not self._values:
            return None

        return self._values[0]

    def last(self) -> Any:
        if not self._values:
            return None

        return self._values[-1]

    def map(self, callback: Callable) -> 'Fluent':
        mapped = map(callback, self._values)

        if isinstance(self._values, Tuple):
            return Fluent(tuple(mapped))

        return Fluent(list(mapped))

    def filter(self, callback: Callable) -> 'Fluent':
        filtered = filter(callback, self._values)

        if isinstance(self._values, Tuple):
            return Fluent(tuple(filtered))

        return Fluent(list(filtered))
