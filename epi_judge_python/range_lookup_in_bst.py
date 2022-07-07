import collections
from typing import List
from unittest import result

from bst_node import BstNode
from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))

# recursive call
# if tree is None, return
# if tree.data inside range:
# append
# lookup left and right (rec)
# if tree.data < interval.left : lookup right
# if tree.data > iterval.right : lookup left


def range_lookup_in_bst(tree: BstNode, interval: Interval) -> List[int]:

    def lookup(node: BstNode) -> None:
        if node is None:
            return
        if interval.left <= node.data <= interval.right:
            lookup(node.left)
            result.append(node.data)
            lookup(node.right)
        elif interval.left > node.data:
            lookup(node.right)
        else:
            lookup(node.left)

    result = []

    lookup(tree)

    return result


def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('range_lookup_in_bst.py',
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
