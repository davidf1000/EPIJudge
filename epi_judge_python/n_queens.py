from typing import List

from test_framework import generic_test

# recursive
# create result, and curr_placement
# base : row == n : correct, append curr placement
# else: for col in range(n):
# check if each column pos is suitable
# if suitable, then add column pos at row pos and call for n+1 (higher row)

# function (row, col) -> check if col placement in a certain row is valid
# check from all previous queen in prev. row, for i,idx in curr_placement[:row]:
# 1. cannot be bottom from prev queen, i != col
# 2. Cannot diagonal, row each row, diff = abs(row, idx), col != (col - diff) or col != (col +diff)


def n_queens(n: int) -> List[List[int]]:
    def compute_position(row: int) -> None:
        if row == n:
            result.append(list(curr_placement))
            return
        for potential_col in range(n):
            if is_suitable_pos(row, potential_col):
                curr_placement[row] = potential_col
                compute_position(row+1)

    def is_suitable_pos(row: int, potential_col: int) -> bool:
        # print("curr_placement :", curr_placement)
        # print("row :", row, "potential_col", potential_col)
        for prev_row, prev_column in enumerate(curr_placement[:row]):
            if prev_column == potential_col:
                return False
            dif = abs(row -  prev_row)
            if potential_col == (prev_column - dif) or potential_col == (prev_column + dif):
                return False
        return True

    result = []
    curr_placement = [0]*n
    compute_position(0)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
