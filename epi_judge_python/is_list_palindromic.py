from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    # Edge case 
    if not L or not L.next:
        return True
    # get half of the array (first is 1//n +1 if n is odd)
    slow = fast = L
    while fast and fast.next:
        fast = fast.next.next
        if fast is None or fast.next is None:
            temp = slow
        slow = slow.next
    if fast is not None:
        slow = slow.next
        temp = temp.next
    temp.next = None
    # Reverse list 
    current = None
    while slow:
        temp = slow.next
        slow.next = current
        current = slow
        slow = temp
    # loop until not current or not L
    while current and L:
        if current.data != L.data:
            return False
        current,L= current.next,L.next
    return True


if __name__ == '__main__':
    # L = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7)))))))
    # print(is_linked_list_a_palindrome(L))
    # exit()
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
