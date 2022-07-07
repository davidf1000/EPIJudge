import functools
from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import (binary_tree_height,
                                              generate_inorder)
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# build bst recursively
# base : len == 0 -> return None
# get middle item, put it on top node, call build for left and right subarray recursively


def build_min_height_bst_from_sorted_array(A: List[int]) -> Optional[BstNode]:
    if len(A) == 0:
        return None
    if len(A) == 1:
        return BstNode(A[0])
    mid_idx = len(A)//2
    return BstNode(A[mid_idx], build_min_height_bst_from_sorted_array(A[:mid_idx]),
                   build_min_height_bst_from_sorted_array(A[mid_idx + 1:]))


@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(
        functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure('Result binary tree mismatches input array')
    return binary_tree_height(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'bst_from_sorted_array.py', 'bst_from_sorted_array.tsv',
            build_min_height_bst_from_sorted_array_wrapper))
