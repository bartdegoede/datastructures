class Deque(object):
    def __init__(self):
        self._values = []

    def add_rear(self, item):
        self._values.insert(0, item)

    def add_front(self, item):
        self._values.append(item)

    def remove_rear(self):
        return self._values.pop(0)

    def remove_front(self):
        return self._values.pop()

    @property
    def empty(self):
        return self._values == []

    @property
    def size(self):
        return len(self._values)


if __name__ == '__main__':
    d = Deque()
    assert(d.empty == True)
    d.add_rear(4)
    assert(d._values == [4])
    d.add_rear('dog')
    assert(d._values == ['dog', 4])
    d.add_front('cat')
    assert(d._values == ['dog', 4, 'cat'])
    d.add_front(True)
    assert(d._values == ['dog', 4, 'cat', True])
    assert(d.size == 4)
    assert(d.empty == False)
    d.add_rear(8.4)
    assert(d._values == [8.4, 'dog', 4, 'cat', True])
    assert(d.remove_rear() == 8.4)
    assert(d.remove_front() == True)
