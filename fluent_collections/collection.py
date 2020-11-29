from typing import Union, Tuple, List, Callable, Any


class Collection:
    _values: Union[List, Tuple]

    def __init__(self, values=None):
        if values is None:
            values = []
        self._values = values

    def is_empty(self) -> bool:
        return not self._values

    def count(self) -> int:
        return len(self._values)

    def all(self) -> Union[List, Tuple]:
        return self._values

    def first(self) -> Any:
        if not self._values:
            return None

        return self._values[0]

    def last(self) -> Any:
        if not self._values:
            return None

        return self._values[-1]

    def map(self, callback: Callable) -> 'Collection':
        mapped = map(callback, self._values)

        if isinstance(self._values, Tuple):
            return Collection(tuple(mapped))

        return Collection(list(mapped))

    def filter(self, callback: Callable) -> 'Collection':
        filtered = filter(callback, self._values)

        if isinstance(self._values, Tuple):
            return Collection(tuple(filtered))

        return Collection(list(filtered))


def collect(items=None):
    if items is None:
        return Collection([])
    return Collection(items)
