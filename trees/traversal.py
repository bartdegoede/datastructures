def inorder(node):
    if node is not None:
        inorder(node.left)
        node.visit()
        inorder(node.right)


def preorder(node):
    if node is not None:
        node.visit()
        preorder(node.left)
        preorder(node.right)


def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        node.visit()
