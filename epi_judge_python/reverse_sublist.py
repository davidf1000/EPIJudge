from turtle import left
from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist_manual(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if not L:
        return None
    # tranverse until start-1 
    # save node before reverse
    # tranverse 1 step 
    # save start node
    # tranverse f-s step
    # save finish node 
    # start node -> node after finish node
    # finish node -> node before start node
    tail = L
    for _ in range(start-2):
        L = L.next
    node_before_start = L
    # create temp
    L = L.next
    temp = ListNode(L.data)
    node_start = temp
    for _ in range(finish-start):
        L = L.next
        temp = ListNode(L.data,temp)
    node_finish = temp
    L = L.next
    node_after_finish = L
    node_before_start.next = node_finish
    node_start.next = node_after_finish
    return tail

def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if not L or not L.next:
        return L 
    # create dummy head
    dummy_head= ListNode(0,L)
    # previous and current
    prev, cur = dummy_head, L
    # loop left-1 times
    for _ in range(1,start):
        prev , cur = cur,cur.next
    left_prev = prev 
    prev = None
    for _ in range(finish-start+1):
        # temp = current.next 
        # current.next -> prev 
        # prev -> current 
        # current -> current.next
        temp = cur.next
        cur.next = prev
        prev, cur = cur,temp
    # prev.next to LP
    # LP.next.next to current
    left_prev.next.next = cur
    left_prev.next = prev
    return dummy_head.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
    A = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,None))))))
    A = ListNode(0,None)
    print(reverse_sublist(A,3,5))