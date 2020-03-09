class Threadable:
    def __init__(self, values = []):
        self._values = values

    def first(self):
        return self._values[0]

    def isEmpty(self):
        return not self._values
