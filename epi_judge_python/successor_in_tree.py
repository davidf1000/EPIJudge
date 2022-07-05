import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def find_successor(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # inorder priority left - root - right 
    # 1st - check if there's right, if yes tranverse, then left until no left, last is node
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    # 2nd - if there's no right, backtrack until parent.left == node
    while node.parent:
        if node.parent.left is node:
            return node.parent
        node = node.parent
    return None


@enable_executor_hook
def find_successor_wrapper(executor, tree, node_idx):
    node = must_find_node(tree, node_idx)

    result = executor.run(functools.partial(find_successor, node))

    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('successor_in_tree.py',
                                       'successor_in_tree.tsv',
                                       find_successor_wrapper))
