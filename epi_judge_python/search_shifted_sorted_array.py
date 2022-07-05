from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    left,right = 0, len(A)-1
    while left<right:
        m = (left+right)//2
        if A[m] < A[right]: #still ascending, cut to left 
            right = m
        else: #A[m] > A[right], cut to right
            left = m+1
    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
