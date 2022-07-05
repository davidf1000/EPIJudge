from multiprocessing import dummy
from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    # while L1 or L2 or Carry
    # add L1.data + L2 data + carry, then append to dummy 
    dummy_head = current = ListNode()
    carry = 0 
    while L1 or L2 or carry:
        sum = (L1.data if L1 else 0) + (L2.data if L2 else 0)+ carry
        carry = sum//10
        sum = sum % 10
        # append to current
        current.next = ListNode(sum)
        current = current.next
        L1,L2 = L1.next if L1 else None,L2.next if L2 else None
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
