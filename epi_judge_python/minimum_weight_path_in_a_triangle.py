from typing import List

from test_framework import generic_test

# DP memoization
# create DP Cache,
# DP[(0,0)] = triangle[0][0]
# recursive
# base : meet bottom idx -> save the total weight, save to cache
# if position already in cache, use cache
# else:
# call recursive for next level with col idx and col idx+1


def minimum_path_weight(triangle: List[List[int]]) -> int:
    DP = {(0, 0): triangle[0][0]}
    

    def recursive(total_weight: int, row: int, col: int) -> None:
        if row == len(triangle)-1:
            DP[(row, col)] = DP.get((row, col), 0) + \
                total_weight + triangle[row][col]
            min_path = min(min_path, DP[(row, col)])
            return DP[(row, col)]
        if (row, col) in DP:
            DP[(row, col)] = DP.get((row, col), 0) + total_weight
            min_path = min(min_path, DP[(row, col)])
            return DP[(row, col)]
        else:
            DP[(row, col)] = min(recursive(total_weight+triangle[row][col], row+1, col),
                                 recursive(total_weight+triangle[row][col], row+1, col+1))
            return DP[(row, col)]
            
    min_path = float('inf')
    recursive(0, 0, 0)
    return min_path


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_weight_path_in_a_triangle.py',
            'minimum_weight_path_in_a_triangle.tsv', minimum_path_weight))
