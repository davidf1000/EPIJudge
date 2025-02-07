from copy import copy, deepcopy
import functools
from typing import List, Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# recursive calls
#

def generate_all_binary_trees(num_nodes: int
                              ) -> List[Optional[BinaryTreeNode]]:
    if num_nodes == 0:
        return [None]
    if num_nodes == 1:
        return [BinaryTreeNode(0)]
    result = []
    for num_left_node in range(num_nodes):
        num_right_node = num_nodes - 1 - num_left_node
        left_subtrees = generate_all_binary_trees(num_left_node)
        right_subtrees = generate_all_binary_trees(num_right_node)
        for node_left in left_subtrees:
            for node_right in right_subtrees:
                result.append(BinaryTreeNode(0, node_left, node_right))
    return result


def serialize_structure(tree):
    result = []
    q = [tree]
    while q:
        a = q.pop(0)
        result.append(0 if not a else 1)
        if a:
            q.append(a.left)
            q.append(a.right)
    return result


@enable_executor_hook
def generate_all_binary_trees_wrapper(executor, num_nodes):
    result = executor.run(
        functools.partial(generate_all_binary_trees, num_nodes))

    return sorted(map(serialize_structure, result))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_trees.py',
                                       'enumerate_trees.tsv',
                                       generate_all_binary_trees_wrapper))
