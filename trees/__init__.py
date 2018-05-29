class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def visit(self):
        print(self)

    def __repr__(self):
        return '{}'.format(self.value)

# A binary search tree is a binary tree where every node fits a specific
# ordering property; all left descendants <= n < all rights. This is true
# for all nodes n.
#
# Not a binary search tree, because 12 is left of 8
#      8
#     / \
#    4   10
#   / \   \
#  2   12  20
binary_tree = Node(8)
binary_tree.left = Node(4)
binary_tree.left.left = Node(2)
binary_tree.left.right = Node(12)
binary_tree.right = Node(10)
binary_tree.right.right = Node(20)
# A binary search tree
#      8
#     / \
#    4   10
#   / \   \
#  2   6  20
binary_search_tree = Node(8)
binary_search_tree.left = Node(4)
binary_search_tree.left.left = Node(2)
binary_search_tree.left.right = Node(6)
binary_search_tree.right = Node(10)
binary_search_tree.right.right = Node(20)
