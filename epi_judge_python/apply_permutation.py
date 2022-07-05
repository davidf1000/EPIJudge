from typing import List

from test_framework import generic_test


# O(n) space
def apply_permutation(perm: List[int], A: List[int]) -> None:
    for i in range(len(perm)):
        if perm[i] == i: #Already in correct pos
            perm[i]-=len(perm)
            continue
        next = i 
        while next>=0:
            temp = perm[i] #destination
            A[i],A[perm[i]] = A[perm[i]],A[i]
            perm[i] -= len(perm)
            perm[i],perm[temp] = perm[temp],perm[i]
            next = temp
    return A


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
    # P = [0,3,1,2]
    # A = ['A','B','C','D']
    # print(apply_permutation(P,A))