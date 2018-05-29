from trees import binary_tree, binary_search_tree
from trees.traversal import inorder, preorder, postorder

if __name__ == '__main__':
    print('In order:')
    inorder(binary_search_tree)
    print('=' * 80)
    print('Preorder:')
    preorder(binary_search_tree)
    print('=' * 80)
    print('Postorder:')
    postorder(binary_search_tree)
