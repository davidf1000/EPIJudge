import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    # count length of both linked list O(n)
    def count_length(head):
        count = 0 
        while head:
            count+=1
            head = head.next
        return count
    if count_length(l0) > count_length(l1):
        longer_list = l0 
        shorter_list = l1 
    else:
        longer_list = l1 
        shorter_list = l0
    # loop longer list until both list have the same length 
    for _ in range(abs(count_length(l0)-count_length(l1))):
        longer_list = longer_list.next
    # loop both list together until null 
    while longer_list and shorter_list:
        longer_list,shorter_list = longer_list.next , shorter_list.next
        if longer_list is shorter_list:
            return longer_list
    return None

@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
