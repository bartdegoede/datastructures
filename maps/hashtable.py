class HashTable(object):
    def __init__(self):
        self.size = 11  # use a prime number
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def rehash(self, h):
        return (h + 1) % self.size

    def _put(self, key, data):
        h = self.hash_function(key)
        # when slot is empty, assign data
        if self.slots[h] is None:
            self.slots[h] = key
            self.data[h] = data
        else:
            if self.slots[h] == key:
                # update the value for existing key
                self.data[h] = data
            else:
                next_slot = self.rehash(h)
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot)

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                self.data[next_slot] = data

    def _get(self, key):
        start = self.hash_function(key)

        stop = False
        position = start

        while self.slots[position] is not None and not stop:
            if self.slots[position] == key:
                return self.data[position]
            else:
                position = self.rehash(position)
                if position == start:
                    return None

    def __getitem__(self, key):
        return self._get(key)

    def __setitem__(self, key, data):
        self._put(key, data)


if __name__ == '__main__':
    h = HashTable()
    h[54] = 'cat'
    h[26] = 'dog'
    h[93] = 'lion'
    h[17] = 'tiger'
    h[77] = 'bird'
    h[31] = 'cow'
    h[44] = 'goat'
    h[55] = 'pig'
    h[20] = 'chicken'
    assert(h.slots == [77, 44, 55, 20, 26, 93, 17, None, None, 31, 54])
    assert(h.data == ['bird', 'goat', 'pig', 'chicken', 'dog', 'lion',
                      'tiger', None, None, 'cow', 'cat'])
    assert(h[20] == 'chicken')
    h[20] = 'mouse'
    assert(h[20] == 'mouse')
    assert(h[99] is None)
