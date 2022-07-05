import functools
from re import L
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def list_pivoting(L: ListNode, x: int) -> Optional[ListNode]:
    # edge cases
    if not L or not L.next:
        return L
    # create 3 dummy 
    # loop while L
    # if bigger/equal/less, add to dummy 
    # append less - equal - dummy
    less_head = less_iter = ListNode()
    equal_head = equal_iter = ListNode()
    more_head = more_iter = ListNode()
    while L:
        if L.data<x:
            less_iter.next = L
            less_iter = less_iter.next
        elif L.data == x :
            equal_iter.next = L
            equal_iter = equal_iter.next
        else:
            more_iter.next = L
            more_iter = more_iter.next
        L = L.next
    more_iter.next = None
    less_iter.next = equal_head.next
    equal_iter.next = more_head.next
    return less_head.next


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pivot_list.py', 'pivot_list.tsv',
                                       list_pivoting_wrapper))
