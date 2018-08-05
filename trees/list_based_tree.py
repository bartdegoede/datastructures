"""
    a
   / \
  b   c
 / \  |
d   e f
"""
tree = [
    'a', #root
        ['b', #left subtree
            ['d', [], []],
            ['e', [], []],
        ],
    ['c', #right subtree
        ['f', [], []],
        []
    ]
]

def binary_tree(r):
    return [r, [], []]

def insert_left(root, new_branch):
    node = root.pop(1)
    if len(node) > 1:
        root.insert(1, [new_branch, node, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right(root, new_branch):
    node = root.pop(2)
    if len(node) > 1:
        root.insert(2, [new_branch, [], node])
    else:
        root.insert(2, [new_branch, [], []])
    return root

def get_root_val(root):
    return root[0]

def set_root_val(root, val):
    root[0] = val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]


if __name__ == '__main__':
    r = binary_tree(3)
    assert(r == [3, [], []])
    insert_left(r, 4)
    assert(r == [3, [4, [], []], []])
    insert_left(r, 5)
    assert(r == [3, [5, [4, [], []], []], []])
    insert_right(r, 6)
    assert(r == [3, [5, [4, [], []], []], [6, [], []]])
    insert_right(r, 7)
    assert(r == [3, [5, [4, [], []], []], [7, [], [6, [], []]]])
    l = get_left_child(r)
    assert(l == [5, [4, [], []], []])
    set_root_val(l, 9)
    assert(l[0] == 9)
    assert(r[1][0] == 9)
    insert_left(l, 11)
    assert(l == [9, [11, [4, [], []], []], []])
