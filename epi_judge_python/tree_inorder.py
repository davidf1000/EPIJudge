from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # create stack to store current node travelled and the collective result 
    res, current = [],[]
    # while tree or current stack is not empty
    while tree or current:
        # prioritize left 
        if tree:
            current.append(tree)
            tree = tree.left
        else: # left and meet None
            tree = current.pop()
            res.append(tree.data)
            # prioritize right, since left give None
            tree = tree.right
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
