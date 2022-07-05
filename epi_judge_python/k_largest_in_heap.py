import heapq
from typing import List

from test_framework import generic_test, test_utils


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    if k <= 0:
        return []
    candidate_max_heap = []
    res = []
    # append first max element
    heapq.heappush(candidate_max_heap, (-A[0], 0))
    # loop for k times
    for _ in range(k):
        # extract the current max di heap
        current_max, current_idx = (
            -candidate_max_heap[0][0], candidate_max_heap[0][1])
        res.append(current_max)
        # pop the max
        heapq.heappop(candidate_max_heap)
        # calculate left(2n+1) and right(2n+2) index in A
        left_idx, right_idx = 2*current_idx+1, 2*current_idx+2
        # if left or right exist, append (val,idx) to max heap
        if left_idx < len(A):
            heapq.heappush(candidate_max_heap,(-A[left_idx],left_idx))
        if right_idx < len(A):
            heapq.heappush(candidate_max_heap,(-A[right_idx],right_idx))
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
