import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
        if not tree:
            return None #edge case
        # base : check if node == node1 or node 2
        # if not, compute result of dfs(left) and dfs(right)
        # if dfs(left)==p and dfs(right)==q :return current node
        # if dfs(left)==p or q and dfs(right)==None:return p or q
        # if dfs(left)==None and dfs(right)= p or q: return p or q
        # else: return None
        def bfs(node:BinaryTreeNode)->BinaryTreeNode:
            if not node:
                return None
            if node.data == node0.data or node.data == node1.data:
                return node
            left, right = bfs(node.left),bfs(node.right)
            if left and right:
                return node
            elif (left and not right) or (right and not left):
                return left or right
        return bfs(tree)

@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
