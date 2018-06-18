class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class List(object):
    def __init__(self, head=None):
        self.head = head

    def add(self, item):
        node = Node(item)
        if self.head:
            node.next = self.head
        self.head = node

    def append(self, item):
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(item)

    def remove(self, item):
        node = self.head
        prev = None
        found = False
        while not found and node:
            if node.value == item:
                found = True
            else:
                prev = node
                node = node.next

        if prev is None:
            # if the node to be deleted is the first one
            self.head = node.next
        else:
            prev.next = node.next

    def search(self, item):
        node = self.head
        while node is not None:
            if node.value == item:
                return True
            node = node.next
        return False

    @property
    def empty(self):
        return self.head is None

    @property
    def size(self):
        c = 0
        node = self.head
        while node is not None:
            c += 1
            node = node.next
        return c

    def index(self, item):
        if self.head:
            node = self.head
            i = 0
            while node.next:
                if node.value == item:
                    return i
                i += 1
                node
