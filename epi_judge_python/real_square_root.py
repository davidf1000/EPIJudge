import math
from test_framework import generic_test


def square_root(x: float,tol:float=1e-9) -> float:
    left, right = (1, x) if x>=1 else (x,1) 
    while not math.isclose(left,right):
        mid = (right+left)*0.5
        mid_squared = mid*mid
        if mid_squared > x:
            right = mid
        else:
            left = mid 
    return left


if __name__ == '__main__':
    print(square_root(6))
    # exit()
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
