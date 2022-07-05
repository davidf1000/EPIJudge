from typing import List

from test_framework import generic_test


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    # TODO - you fill in here.
    matrix_size = len(square_matrix) - 1
    for i in range(len(square_matrix)//2):
        print(f'iteration {i}')
        for j in range(i, matrix_size-i):
            (square_matrix[i][j], square_matrix[i][~j], square_matrix[~i][~j],
             square_matrix[~i][j]) = (square_matrix[i][~j], square_matrix[~i][~j],
                                      square_matrix[~i][j], square_matrix[i][j])
    print(square_matrix)    
    return


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    # exit(
    #     generic_test.generic_test_main('matrix_rotation.py',
    #                                    'matrix_rotation.tsv',
    #                                    rotate_matrix_wrapper))
    T = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate_matrix(T))
