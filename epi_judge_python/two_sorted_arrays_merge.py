from typing import List

from test_framework import generic_test

"""
4 5 6 4 5 6 
^     
           
1 2 3  
    ^

1. Brute force: 
temp []
loop to add B to A from idx n -> n+m-1
then sort
time complexity : O((m+n)log(m+n))

2. using pointer
pointer current from range n+m-1 -> 0
pointer A from range (n-1 -> 0)
pointer B from range (m-1 -> 0)
while i>-1 and j>-1:
    if A[i] > A[j]:
        A[current] = A[i]
        i--
    else:
        A[current] = B[j]
        b--
    current --  
if i==-1: A[:current+1] = A[:i+1]
elif j==-1: A[:current+1] = B[:j+1]
"""

def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    print(A)
    # TODO - you fill in here.
    current, i, j = n+m -1 , m-1, n-1
    print(current,i,j)
    while i>=0 and j>=0:
        if A[i] > B[j]:
            A[current] = A[i]
            i -=1
        else:
            A[current] = B[j]
            j -=1
        current -=1
    while j>=0:
        A[current] = B[j]
        j-=1
        current-=1

def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
