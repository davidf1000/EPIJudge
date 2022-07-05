from cmath import inf
from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    longest = -inf
    setA = set(A)
    while setA:
        item = setA.pop()
        left,right = item-1, item+1
        curr_sum , length = item, 1
        while left in setA or right in setA:
            if left in setA:
                setA.remove(left)
                curr_sum, length, left = curr_sum + left, length + 1, left-1
            if right in setA:
                setA.remove(right)
                curr_sum,length, right = curr_sum + right, length + 1, right +1
        if length > longest: longest = length
    return longest if longest != -inf else 0


if __name__ == '__main__':
    # X = [3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8]
    # print(longest_contained_range(X))
    # exit()
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
