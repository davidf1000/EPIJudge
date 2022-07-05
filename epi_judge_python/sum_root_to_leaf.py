from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    def dfs(node:BinaryTreeNode,prev_sum:int)->int:
        # base 
        if not node:
            return 0
        # compute sum 
        current_sum = prev_sum*2 + node.data
        # if leaf 
        if node and not node.left and not node.right:
            return current_sum
        # if not leaf
        else:
            return dfs(node.left,current_sum) + dfs(node.right,current_sum)
    return dfs(tree,0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
