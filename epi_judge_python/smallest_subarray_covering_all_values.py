from cmath import inf
import collections
import functools
from typing import List
from itertools import cycle
from test_framework import generic_test
from test_framework.test_failure import TestFailure  # keep

from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_sequentially_covering_subset(paragraph: List[str],
                                               keywords: List[str]
                                               ) -> Subarray:
    print()
    if len(keywords) == 0:
        return ''
    key = cycle(keywords)
    first = next(key)
    right = 0 
    min_dist, min_start, min_end = inf, -1, -1
    for left,char in enumerate(paragraph):
        if char == first:
            right = left + 1 
            find = next(key)
            while right < len(paragraph) and right-left<min_dist:
                # if find the next sequential character, next find 
                if paragraph[right] == find:
                    find = next(key)
                # cek base cond, if find == first (assume unique), do len comparison, then break
                if find == first:
                    dist = right - left
                    if dist < min_dist:
                        min_dist, min_start, min_end = dist, left, right
                    break                    
                right +=1 
            # reset until find == again 
            while find != first:
                find = next(key)

    # print(f'result: dist: {min_dist} at p[{min_start},{min_end} = p[{paragraph[min_start]}],{paragraph[min_end]} ]')
    return Subarray(min_start, min_end) if min_dist != inf else ''


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure('Not all keywords are in the generated subarray')
        if para_idx >= len(paragraph):
            raise TestFailure('Subarray end index exceeds array size')
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    # print(find_smallest_sequentially_covering_subset(["S", "O", "B"],["S", "O", "B"]))
    # exit()
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_all_values.py',
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))
