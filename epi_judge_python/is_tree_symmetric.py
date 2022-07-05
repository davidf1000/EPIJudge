from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def dfs(left:BinaryTreeNode,right:BinaryTreeNode)->bool:
        # basis
        if not left and not right:
            return True
        # salah satu empty
        elif (left and not right)or(right and not left):
            return False
        else:
            # simetri if data equal, left.left == right.right, left.right == right.left
            is_symmetrical = (left.data==right.data) and dfs(left.left,right.right) and dfs(left.right,right.left)
            return is_symmetrical
    return not tree or dfs(tree.left,tree.right)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
