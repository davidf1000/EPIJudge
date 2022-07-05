from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    # TODO - you fill in here.
    # create empty list
    # loop for n times
    if not n:
        return[]
    res = [[1]]
    for i in range(1, n):
        temp = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
                continue
            temp.append(res[i-1][j-1]+res[i-1][j])
        res.append(temp)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))

    # print(generate_pascal_triangle(2))
