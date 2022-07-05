import heapq
from typing import List

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    min_heap = []
    # create iterator for sorter arrays
    sorted_array_iter = [iter(x) for x in sorted_arrays]
    # add all first element inside min_hep
    for i,item in enumerate(sorted_array_iter):
        first_element = next(item,None)
        if first_element is not None:
            heapq.heappush(min_heap,(first_element,i))
    # loop until min_heap empty
    res = []
    while min_heap:
        val, i = heapq.heappop(min_heap)
        res.append(val)
        next_element = next(sorted_array_iter[i],None)
        if next_element is not None:
            heapq.heappush(min_heap,(next_element,i))
    return res


if __name__ == '__main__':
    # X = [[-1,0],[-2]]
    # print(merge_sorted_arrays(X))
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
