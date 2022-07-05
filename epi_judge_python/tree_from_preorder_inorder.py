from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    # base 
    if not preorder or not inorder:
        return None
    root = BinaryTreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = binary_tree_from_preorder_inorder(preorder[1:mid+1],inorder[:mid])
    root.right = binary_tree_from_preorder_inorder(preorder[mid+1:],inorder[mid+1:])
    return root


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
