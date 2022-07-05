import collections
import functools
from turtle import right
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))

"""
[-4,-1] [0,2] [3,6] [7,9] [11,12] [14,17]
          1           8

loop while i<len and i.start < s.start and i.end < s.start: until found (i.start < s.start < i.end): 
    i++
start_idx = i
while i<len and not(i.start > s.end and i.end > s.end):
    i++
end_idx = i
if start_idx and end_idx < len, 
    return [:start_idx] + [A[start_idx].start:A[end_idx].end] + [end_idx:] 
elif start < but end_idx >= len : 
    return [:start_idx] + [A[start_idx].start:]
else:
    return normal 
"""


def add_interval(disjoint_intervals: List[Interval],
                 new_interval: Interval) -> List[Interval]:
    if not disjoint_intervals:
        return []
    if not new_interval:
        return disjoint_intervals
    i = 0
    while i < len(disjoint_intervals) and (new_interval.left>disjoint_intervals[i].left or new_interval.left>disjoint_intervals[i].right):
        i += 1
    left_idx = i
    while i < len(disjoint_intervals) and not(disjoint_intervals[i].left >
                                              new_interval.right and disjoint_intervals[i].right > new_interval.right):
        i+=1
    right_idx = i
    print(left_idx,disjoint_intervals[left_idx])
    print(right_idx,disjoint_intervals[right_idx])
    if left_idx<len(disjoint_intervals) and right_idx<len(disjoint_intervals): 
        print('CASE 1')
        left = disjoint_intervals[:left_idx-1] if 
        return disjoint_intervals[:left_idx-1] + [Interval(min(new_interval.left,disjoint_intervals[left_idx-1].left),max(new_interval.right,disjoint_intervals[right_idx-1].right))] + disjoint_intervals[right_idx:]                                              
    elif left_idx<len(disjoint_intervals) and right_idx>=len(disjoint_intervals):
        print('CASE 2')
        return disjoint_intervals[:left_idx] + disjoint_intervals[left_idx:]
    else:
        print('CASE 3',left_idx,right_idx)
        return disjoint_intervals


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    # print(add_interval([Interval(-4,-1),Interval(0,2),Interval(3,6),Interval(7,9),Interval(11,12),Interval(14,17)],Interval(1,8)))
    # exit()
    exit(
        generic_test.generic_test_main('interval_add.py',
                                       'interval_add.tsv',
                                       add_interval_wrapper,
                                       res_printer=res_printer))
