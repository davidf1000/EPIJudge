from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    # base
    if not tree:
        return False
    # compute current remaining weight (preorder)
    current_remaining_weight = remaining_weight - tree.data
    # check if leaf
    if tree and not tree.left and not tree.right:
        return current_remaining_weight == 0
    else:  # if not leaf
        return has_path_sum(tree.left, current_remaining_weight) or has_path_sum(
            tree.right, current_remaining_weight
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
