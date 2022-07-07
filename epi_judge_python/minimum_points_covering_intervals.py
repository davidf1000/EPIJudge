import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))

# track last visit, and number of visit
# sort based on right interval
# loop for interval
# if last visit time < leftmost side:
#   number visit ++
#   last visit = interval.right


def find_minimum_visits(intervals: List[Interval]) -> int:
    last_visit, num_visit = float('-inf'), 0
    intervals.sort(key=lambda x: x.right)
    for interval in intervals:
        if last_visit < interval.left:
            num_visit += 1
            last_visit = interval.right
    return num_visit


@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_points_covering_intervals.py',
            'minimum_points_covering_intervals.tsv',
            find_minimum_visits_wrapper))
