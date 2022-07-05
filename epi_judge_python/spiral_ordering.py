from math import ceil
from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    # Function to peel off offset layer
    def add_layer(offset):
        middle = len(square_matrix)-offset-1==offset
        # check if middle, append the middle only 
        if middle:
            matrix.append(square_matrix[offset][offset])
            return
        # peel left to right 

        matrix.extend(square_matrix[offset][offset:-offset-1])
        # peel top to bottom 
        matrix.extend(
            list(zip(*square_matrix))[-1 - offset][offset:-1 - offset])

        # peel right to left
        matrix.extend(square_matrix[-offset-1][-offset-1:offset:-1])
        # peel bottom to top 
        matrix.extend(
            list(zip(*square_matrix))[offset][-1 - offset:offset:-1])
        return
    
    matrix = []
    # loop for each offset
    for i in range(ceil(len(square_matrix)/2)):
        add_layer(i)

    return matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
    # T = [[4, 2], [3, 1]]
    # print(matrix_in_spiral_order(T))