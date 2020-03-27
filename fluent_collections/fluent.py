from typing import Union, Tuple, List, Callable


class Fluent:
    _values: Union[List, Tuple]

    def __init__(self, values=[]):
        self._values = values

    def is_empty(self):
        return not self._values

    def count(self):
        return len(self._values)

    def all(self):
        return self._values

    def first(self):
        if not self._values:
            return None

        return self._values[0]

    def last(self):
        if not self._values:
            return None

        return self._values[-1]

    def map(self, callback: Callable):
        mapped = map(callback, self._values)

        if isinstance(self._values, Tuple):
            return tuple(mapped)

        return list(mapped)

    def filter(self, callback: Callable):
        filtered = filter(callback, self._values)

        if isinstance(self._values, Tuple):
            return tuple(filtered)

        return list(filtered)
