import functools
from typing import List
from venv import create

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    # edge case 
    if not tree:
        return []
    # create function to get left and right edges 
    # true for left, false for right
    def create_edges_left(node: BinaryTreeNode)->list:
        temp = []
        # while loop until leaf
        while node.left or node.right:
            # print('temp',temp,node.left,node.right)
            if node.left:
                temp.append(node)
                node = node.left
            elif node.right:
                temp.append(node)
                node = node.right
        # return without root node for right
        return temp
    def create_edges_right(node: BinaryTreeNode)->list:
        temp = []
        # while loop until leaf
        while node.left or node.right:
            # print('temp',temp,node.left,node.right)
            if node.right:
                temp.append(node)
                node = node.right
            elif node.left:
                temp.append(node)
                node = node.left
        # return without root node for right
        return temp[::-1]     
    mid = []
    # create function to get leaves 
    def get_leaves(node:BinaryTreeNode)->None:
        # base 
        if not node:
            return
        if not node.left and not node.right:
            mid.append(node)
        # tranverse left right
        get_leaves(node.left)
        get_leaves(node.right)
        return
    get_leaves(tree)
    mid = mid if (tree.left or tree.right) else []
    left = create_edges_left(tree)[1:] if tree.left else []
    right = create_edges_right(tree)[:-1] if tree.right else []
    # print('\n,left',[x.data for x in left])
    # print('\nmid',[x.data for x in mid])
    # print('\nright',[x.data for x in right])
    return [tree]+ left + mid + right


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    # A = BinaryTreeNode(2,BinaryTreeNode(3),BinaryTreeNode(4))
    # B = BinaryTreeNode(5,BinaryTreeNode(6),BinaryTreeNode(7))
    # C = BinaryTreeNode(1,A,B)
    # print(C)
    # print(exterior_binary_tree(C))
    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
