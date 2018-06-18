class BasicQueue(object):
    def __init__(self):
        self._values = []

    @property
    def empty(self):
        return self._values == []

    @property
    def size(self):
        return len(self._values)

    def enqueue(self, item):
        self._values.insert(0, item)

    def dequeue(self):
        return self._values.pop()


if __name__ == '__main__':
    q = BasicQueue()
    assert(q.empty == True)
    assert(q.size == 0)
    q.enqueue(4)
    assert(q._values == [4])
    q.enqueue('dog')
    assert(q._values == ['dog', 4])
    q.enqueue(True)
    assert(q._values == [True, 'dog', 4])
    assert(q.size == 3)
    assert(q.empty == False)
    q.enqueue(8.4)
    assert(q._values == [8.4, True, 'dog', 4])
    assert(q.dequeue() == 4)
    assert(q._values == [8.4, True, 'dog'])
    assert(q.dequeue() == 'dog')
    assert(q._values == [8.4, True])
    assert(q.size == 2)
