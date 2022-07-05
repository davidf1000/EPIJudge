import functools
from turtle import distance
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    def has_cycle(head: ListNode)-> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next , slow.next
            # if they met, then has cycle 
            if fast is slow:
                # find the head node
                slow = head
                while slow is not fast:
                    slow, fast = slow.next, fast.next
                return slow
        return None
    def count_size(head: ListNode)-> int:
        # only for uncyclic
        count = 0 
        while head:
            count +=1
            head = head.next
        return count
    # Check Case 
    # Case 1 : L0 and L1 have no cycle -> Do normal check 
    is_l0_cyclic, is_l1_cyclic = has_cycle(l0), has_cycle(l1)
    if not is_l0_cyclic and not is_l1_cyclic:
        # check which one is bigger (assume l0 bigger)
        # tranverse l0 for len(l0)-len(l1) times
        # tranverse both until null
        l0_size, l1_size = count_size(l0),count_size(l1)
        (l0,l1) = (l0,l1) if l0_size>l1_size else (l1,l0)
        for _ in range(l0_size-l1_size):
            l0 = l0.next
        while l0 and l1 and l0 is not l1:
            l0, l1 = l0.next, l1.next
        return l0 # return None if doesn't overlap
    # Case 2 : one list is cyclic and one list is not -> will not overlap 
    if (is_l0_cyclic and not is_l1_cyclic) or (is_l1_cyclic and not is_l0_cyclic):
        return None
    # Case 3 : both list is cyclic -> check if the cycle is identical 
    # tranverse from head of one list until find root or root2
    temp  = is_l1_cyclic
    while True:
        temp = temp.next
        if temp is is_l0_cyclic or temp is is_l1_cyclic:
            break
    return is_l1_cyclic if temp is is_l0_cyclic else None
    # def calculate_distance(a: ListNode,b: ListNode)-> int:
    #     dis = 0 
    #     while a is not b:
    #         dis+=1 
    #         a = a.next
    #     return dis
    # # Case 3a : path to cycle merge before cycle -> Check normally 
    # # Case 3b: path to cycle merge after cycle 
    # # check distance from head to root for each list 
    # dist0, dist1 =calculate_distance(l0,is_l0_cyclic), calculate_distance(l1,is_l1_cyclic)
    # (l0,is_l0_cyclic,l1,is_l1_cyclic) = (l0,is_l0_cyclic,l1,is_l1_cyclic) if dist0>dist1 else (l1,is_l1_cyclic,l0,is_l0_cyclic) 
    # for _ in range(dist0-dist1):
    #     l0 =l0.next
    # while l0 is not l1 and l0 is not is_l0_cyclic and l1 is not is_l1_cyclic:
    #     l0,l1 = l0.next, l1.next
    # return l0 if l0 is l1 else is_l0_cyclic 


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
