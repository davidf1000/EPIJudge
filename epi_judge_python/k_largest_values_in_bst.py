from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils

# count = k
# do reverse postorder, start from right
# base: count === 0 : return
# base case : node has no child -> append node, k--
# recursive call from right, then left


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    if not tree:
        return []
    k_largest = []

    def reverse_inorder(node: BstNode) -> None:
        if (len(k_largest) == k or not node):
            return
        reverse_inorder(node.right)
        if (len(k_largest) < k):
            k_largest.append(node.data)
        reverse_inorder(node.left)

    reverse_inorder(tree)
    return k_largest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
