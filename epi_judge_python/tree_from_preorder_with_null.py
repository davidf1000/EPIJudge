import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    def reconstruct(pre_iter:iter)->BinaryTreeNode:
        root = next(pre_iter)
        # base 
        if not root:
            return None
        # create left and right subtree
        root = BinaryTreeNode(root)
        root.left = reconstruct(pre_iter)
        root.right = reconstruct(pre_iter)
        return root
    return reconstruct(iter(preorder))


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
