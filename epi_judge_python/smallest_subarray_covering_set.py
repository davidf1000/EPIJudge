from ast import Sub
from cmath import inf
import collections
import functools
import itertools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    if len(keywords) == 0:
        return ''
    # hashmap for keyword and window
    # left pointer
    # need and have
    # min dist and idx
    window, map_keyword = {}, {}
    left = 0
    min_dist, min_start, min_end = inf, -1, -1
    # fill map and window
    for item in keywords:
        map_keyword[item] = map_keyword.get(item, 0) + 1
        window[item] = 0
    need, have = len(map_keyword), 0
    for r, char in enumerate(paragraph):
        # ++ counter window
        if char in map_keyword:
            window[char] = 1 + window.get(char, 0)
            # update have if ++ make it surpasses requirement and char in map
            if window[char] == map_keyword[char]:
                have += 1
        # if have == need, keep moving left >>, if in map --, check if it makes have decreases
        while have == need and left <= r:
            char_left = paragraph[left]
            # update min
            dist = r - left
            if dist < min_dist:
                min_dist, min_start, min_end = dist, left, r
            if char_left in map_keyword:
                window[char_left] -= 1
                if window[char_left] < map_keyword[char_left]:
                    have -= 1
            # move left >>
            left += 1
    return Subarray(min_start, min_end) if min_dist != inf else ''


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    # print(find_smallest_subarray_covering_set(['a','b','c','b','d','x','y','z','b'],{'b','d','c'}))
    # exit()
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
