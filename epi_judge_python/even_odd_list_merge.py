from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    # edge case 
    if not L or not L.next:
        return L
    count = 0 
    head = L 
    while head:
        head  = head.next
        count +=1 
    current = L
    first_head = first = ListNode(0)
    second_head = second =  ListNode(0)
    for i in range(count):
        # if even, add node to first, advance current, then first.next = None
        # if odd, add node to second, advance current, second.next = None
        if i%2==0:
            first.next = current
            current = current.next
            first = first.next
            first.next= None
        else:
            second.next = current
            current = current.next
            second=second.next
            second.next= None
    first.next = second_head.next
    return first_head.next


if __name__ == '__main__':
    # L = ListNode(0,ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))))
    # print(even_odd_merge(L))
    # exit()
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
