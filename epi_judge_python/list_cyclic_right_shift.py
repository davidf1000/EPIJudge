from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    # Edge case
    if not L or not L.next:
        return L
    # function to count len 
    def count_size(x:ListNode) -> int :
        count = 0 
        while x:
            count +=1
            x = x.next
        return count
    k = k % count_size(L)
    if k==0:
        return L
    # get dummy node and first element node
    dummy = ListNode(0,L)
    first_node = dummy.next
    # get sublist with head and tail
    a = b = L
    for _ in range(k):
        b = b.next
    while b.next:
        a,b = a.next,b.next
    # Advance a by 1, and unlink node before a
    temp = a 
    a = a.next
    temp.next = None
    dummy.next = a 
    b.next = first_node 
    # dummy.next = head, tail.next = first element node 
    return dummy.next


if __name__ == '__main__':
    # E = [2, 3, 5, 6, 10, 9, 1, 11, 4, 8, 7]
    # head = dummy = ListNode(0,None)
    # for i in E:
    #     dummy.next = ListNode(i)
    #     dummy = dummy.next
    # print(head)
    # head = head.next
    # print(cyclically_right_shift_list(head,9))
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
