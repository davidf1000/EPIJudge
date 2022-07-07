from typing import List

from test_framework import generic_test

import bintrees

# track the min_dist
# store each of first element (smallest) inside bintree (also track their idx order 0 1 2)
# loop until one of the array is empty


def find_closest_elements_in_sorted_arrays(sorted_arrays: List[List[int]]
                                           ) -> int:
    min_dist = float('inf')
    # store array
    binaryTree = bintrees.RBTree()
    for idx, sorted_array in enumerate(sorted_arrays):
        iter_array = iter(sorted_array)
        smallest_element = next(iter_array, None)
        if smallest_element is not None:
            binaryTree.insert((smallest_element, idx), iter_array)
    while True:
        min_val, min_idx = binaryTree.min_key()
        max_val, max_idx = binaryTree.max_key()
        min_dist = min(max_val-min_val, min_dist)
        it = binaryTree.pop_min()[1]
        next_min = next(it, None)
        if next_min is None:
            return min_dist
        binaryTree.insert((next_min, min_idx), it)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_distance_3_sorted_arrays.py',
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
