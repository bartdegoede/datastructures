from heap import Heap

def run():
    heap = Heap()
    data = [0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
    size = len(data[1:])
    heap._heap = data
    assert(heap.size == size)
    heap.insert(7)
    assert(heap._heap[2] == 7)
    assert(heap.size == size + 1)
    smallest_value = heap.delete_min()
    assert(smallest_value == 5)
    assert(heap.size == size)

if __name__ == '__main__':
    run()
