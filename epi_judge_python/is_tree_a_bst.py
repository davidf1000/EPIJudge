from cmath import inf
from msilib.schema import Binary
from operator import truediv
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# TODO - you fill in here.
# base base: node is none, return true
# node is
# postorder : true if is_bst(tree.left) and is_bst(tree.right)
# and tree.left.data <= tree.data <= tree.right.data

# create recursive func with low and high range
# base case -> if none return true
# if tree data not in range low-high -> return False
# postorder -> return is_bst(left) and is_bst(right)


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def is_bst(node: BinaryTreeNode, low: int, high: int) -> bool:
        if not node:
            return True
        if not(low <= node.data <= high):
            return False
        return is_bst(node.left, low, node.data) and is_bst(
            node.right, node.data, high
        )
    return is_bst(tree, float('-inf'), float('inf'))

# time: O(n)
# space : O(n) -> if BST skewed


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
