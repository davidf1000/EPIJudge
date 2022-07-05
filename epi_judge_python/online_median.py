import heapq
from typing import Iterator, List

from test_framework import generic_test


def online_median(sequence: Iterator[int]) -> List[float]:
    # left side array -> max_heap
    # right side array -> min_heap
    # if even, len left == len right. if odd, len left -1 == len right 
    left_max_heap, right_min_heap = [] , [] 
    res = []
    for item in sequence:
        heapq.heappush(left_max_heap,- heapq.heappushpop(right_min_heap,item))
        if len(left_max_heap)-len(right_min_heap) ==2:
            heapq.heappush(right_min_heap,- heapq.heappop(left_max_heap))
        median = -left_max_heap[0] if len(left_max_heap)>len(right_min_heap) else (-left_max_heap[0]+right_min_heap[0])/2 
        res.append(median)
    return res


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    # print(online_median_wrapper([5,4,3,2,1]))
    # exit()
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
