from typing import Union, Tuple, List


class Fluent:
    _values: Union[List, Tuple]

    def __init__(self, values=[]):
        self._values = values

    def first(self):
        return self._values[0]

    def is_empty(self):
        return not self._values
