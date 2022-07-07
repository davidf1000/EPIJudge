from typing import List

from test_framework import generic_test

# set i,j as the edge
# while i<j :
# count the max water trapped
# compare with the current max
# check if height[i] < height [j], i++
# else j--


def get_max_trapped_water(heights: List[int]) -> int:
    i, j, max_water = 0, len(heights) - 1, 0
    while i < j:
        curr_max_water = (j-i) * min(heights[i], heights[j])
        max_water = max(max_water, curr_max_water)
        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1
    return max_water


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
