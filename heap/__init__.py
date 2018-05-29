class Heap(object):
    """
    Heaps are complete binary trees. That means that we can store the tree
    as a list, where the children of a value stored at index p are stored at
    indices 2p and 2p+1:

               5
           /      \
          9       11
        /   \    /  \
      14    18  19  21
     /  \   /
    33  17 27
    [0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27, ...]

    http://interactivepython.org/courselib/static/pythonds/Trees/BinaryHeapImplementation.html
    """
    def __init__(self):
        # initialize with 0 value; will not be used, but will give us access
        # to integer division
        self._heap = [0]

    def insert(self, value):
        self._heap.append(value)
        self._percolate_up(self.size)

    def delete_min(self):
        # smallest value
        value = self._heap[1]
        # replace smallest value by moving the last item into root position
        self._heap[1] = self._heap.pop()
        self._percolate_down(1)
        return value

    @property
    def size(self):
        return len(self._heap) - 1

    def _swap(self, node1, node2):
        tmp = self._heap[node1]
        self._heap[node1] = self._heap[node2]
        self._heap[node2] = tmp

    def _percolate_up(self, i):
        while i // 2 > 0:
            # the parent of self._heap[i] is always an integer division by 2
            # away; values stored at index 10 or 11 have a parent at index 5
            parent = i // 2
            if self._heap[i] < self._heap[parent]:
                self._swap(i, parent)
            i = parent

    def _percolate_down(self, i):
        while (i * 2) <= self.size:
            smallest_child = self._smallest_child(i)
            if self._heap[i] > self._heap[smallest_child]:
                self._swap(i, smallest_child)
            i = smallest_child

    def _smallest_child(self, i):
        if i * 2 + 1 > self.size:
            # if the current node doesn't have a right child, return the
            # left child
            return i * 2
        else:
            if self._heap[i*2] < self._heap[i*2+1]:
                # the smallest child is the left child
                return i * 2
            else:
                return i * 2 + 1
