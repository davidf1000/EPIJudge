from typing import List

from test_framework import generic_test

"""
general idea : start with rightmost digit, if>9 overflow, use overflow for the next digit
                if already the leftmost digit, append overflow from left

reverse(A)
reverse(B)
ovf, sum = 0 , 0
for i,j in len(A,B):
    sum = A[i] + B[i] + ovf
    A[i] = sum % 10 
    ovf = 1 if sum>9 else 0
reverse(A)

O(n)
"""

def plus_one(A: List[int]) -> List[int]:
    A.reverse()
    ovf,sum = 1,1
    for i in range(len(A)):
        sum = A[i] + ovf
        A[i] = sum % 10
        ovf = 1 if sum>9 else 0 
        if ovf == 0:
            break
        if i == len(A)-1:
            A.append(1)
    A.reverse()
    print(A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
    # X = [9,9,9]
    # plus_one(X)
