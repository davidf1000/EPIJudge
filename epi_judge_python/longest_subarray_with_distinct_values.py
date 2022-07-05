from cmath import inf
from typing import List

from test_framework import generic_test


def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    if not A: #edge case 
        return 0
    hashmap = {}
    left = 0 
    longest = -inf
    for right,char in enumerate(A):
        # put char in hashmap, if current_len > 1: then go loop
        # while current_len >1, keep moving left until find the dupli char at idx i,
        # then update hashmap and move left to i+1 
        hashmap[char] = hashmap.get(char,0) + 1 
        while hashmap[char] > 1 and left<right :
            # decrement hashmap
            hashmap[A[left]] -=1
            left += 1
        # update longest
        dist = right-left+1
        if dist>longest: longest=dist
    return longest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
