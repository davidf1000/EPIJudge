from dataclasses import dataclass
from multiprocessing import dummy
from typing import Optional, Set

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    if not L or not L.next : 
        return L
    # create a b pointer
    a = b = L
    b = b.next
    while a:
        while b and b.data == a.data:
            b = b.next
        a.next = b
        a = a.next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
