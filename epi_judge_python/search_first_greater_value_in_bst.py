from typing import Optional

from bst_node import BstNode
from test_framework import generic_test

# track current node and closest_to_k
# while node is not None,
# if data > k -> save number to closest, proceed to left (try finding closer num)
# else (data < k) -> no hope if going left, go right


def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    curr_node, closest_k = tree, None
    while (curr_node):
        if curr_node.data > k:
            closest_k = curr_node
            curr_node = curr_node.left
        else:
            curr_node = curr_node.right
    return closest_k


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
