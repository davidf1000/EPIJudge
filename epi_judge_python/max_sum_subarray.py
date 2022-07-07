from typing import List

from test_framework import generic_test

# track the min_sum and max_sum of current subarray
# loop for each item
# calculate the sum
# min_sum = min(min_sum, sum)
# max_sum = max(max_sum, sum- min_sum)

def find_maximum_subarray(A: List[int]) -> int:
    # TODO - you fill in here.
    min_sum , max_sum = 0, 0
    curr_sum = 0
    for item in A :
        curr_sum += item 
        min_sum = min(min_sum, curr_sum)
        max_sum = max(max_sum, curr_sum - min_sum)
    return max_sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
