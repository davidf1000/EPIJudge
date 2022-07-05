from functools import partial
from typing import List
import math
from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # TODO - you fill in here.
    def has_duplicate(x):
        x = list(filter(lambda a:a!=0,x))
        return len(x) != len(set(x))

    n = len(partial_assignment)
    # check row and column
    if any(
        has_duplicate([partial_assignment[i][j] for j in range(n)]) or 
        has_duplicate([partial_assignment[j][i] for j in range(n)]) 
        for i in range(n)
    ):
        return False
    # check 3x3 grid 
    region_size = int(math.sqrt(n))
    if any(
        has_duplicate(
            [partial_assignment[a][b]
            for a in range(region_size*i,region_size*(i+1))
            for b in range(region_size*j,region_size*(j+1))] 
            )
         for i in range(region_size) for j in range(region_size)):
        return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                        'is_valid_sudoku.tsv', is_valid_sudoku))
