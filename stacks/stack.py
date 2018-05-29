class Stack(object):
    def __init__(self):
        self._values = []

    def push(self, value):
        self._values.append(value)

    def pop(self):
        return self._values.pop()

    def peek(self):
        return self._values[-1]

    def is_empty(self):
        return len(self._values) <= 0

    def size(self):
        return len(self._values)

    def __repr__(self):
        return '{}'.format(self._values)
