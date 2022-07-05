from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
    cur, res = [],[]
    while cur or tree:
        if tree:
            cur.append(tree)
            res.append(tree.data)
            tree = tree.left
        else:
            tree = cur.pop()
            tree = tree.right
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_preorder.py', 'tree_preorder.tsv',
                                       preorder_traversal))
