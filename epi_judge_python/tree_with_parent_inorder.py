from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    prev, res = None, []
    while tree:
        # kasus lagi turun 
        if tree.parent is prev:
            if tree.left:
                next = tree.left
            else:
                res.append(tree.data)
                next = tree.right or tree.parent
        # kasus lagi naik dan prev nya dari kiri
        elif tree.left is prev:
            # inorder, langsung append
            res.append(tree.data)
            next = tree.right or tree.parent
        # kasus else: gak bisa ngapa"in lagi di node ini 
        else:
            next = tree.parent
        prev = tree
        tree = next 
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
