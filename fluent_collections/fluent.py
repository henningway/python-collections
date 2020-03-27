from typing import Union, Tuple, List


class Fluent:
    _values: Union[List, Tuple]

    def __init__(self, values=[]):
        self._values = values

    def is_empty(self):
        return not self._values

    def first(self):
        if not self._values:
            return None

        return self._values[0]

    def last(self):
        if not self._values:
            return None

        return self._values[-1]


