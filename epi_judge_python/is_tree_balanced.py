from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def dfs(root:BinaryTreeNode)->(bool,int):
        # basis
        if not root:
            return (True,0)
        left,right = dfs(root.left),dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1]-right[1])<=1
        return (balanced,1+max(left[1],right[1]))
    return dfs(tree)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
