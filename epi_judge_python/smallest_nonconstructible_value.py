from typing import List

from test_framework import generic_test


"""
- Brute Force
loop for 1-n, -- from the biggest
O(n^2)

[1] = 1, max u = 1 
[1,1] = 1 - 2 -> u (max generated) = 2 
[1,2] = 1 - 3 -> u+1 == v, max increased to u+v 
[1,3] = 1,3, 4 -> u+1 < v, theres a gap in u+1 
[1,2,3] = [1,2,3,4,5,6], u = 3, v = 3, can generate up to u+v (if v<=u+1)

algo :
u = A[0]
loop for every element in 1,len(A): 
    if A[i]<=u: u += A[i]
    else: break
reach the end of element and still able, 
return u+1
Time complexity O(n), Space O(1)
"""


def smallest_nonconstructible_value(A: List[int]) -> int:
    A.sort()
    if not A: return 1
    u = 0
    for i in range(len(A)):
        if A[i] <= u+1: u+= A[i]
        else:
            break
    return u+1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('smallest_nonconstructible_value.py',
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
