from typing import List, Optional

from list_node import ListNode, list_size
from test_framework import generic_test


def merge_two_sorted_lists_default(L1: Optional[ListNode],
                                   L2: Optional[ListNode]) -> Optional[ListNode]:
    # Create dummy head
    dummy_head = tail = ListNode()
    # Loop for L1 and L2
    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
        tail = tail.next

    tail.next = L1 or L2
    return dummy_head.next


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    tail = L1
    while L1.next:
        L1 = L1.next
    # Last Node
    L1.next = L2
    # dummy head
    print(list_size(tail))
    for i in range(list_size(tail)):
        for j in range(list_size(tail)-i):
            if
    return tail
    # loop L1
    # Combine with L2
    # print


if __name__ == '__main__':
    # exit(
    #     generic_test.generic_test_main('sorted_lists_merge.py',
    #                                    'sorted_lists_merge.tsv',
    #                                    merge_two_sorted_lists))

    A = ListNode(1, ListNode(5, ListNode(2)))
    B = ListNode(4, ListNode(5, ListNode(3)))
    print(A)
    print(B)
    print(merge_two_sorted_lists(A, B))
