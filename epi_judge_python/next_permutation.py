from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    # find the rightmost that doesnt ascending 
    pivot = -1
    for i in reversed(range(len(perm)-1)):
        if perm[i]<perm[i+1]:
            pivot = i 
            break
    if pivot==-1:
        return []
    # swap that with rightmost greater than pivot
    for i in reversed(range(pivot,len(perm))):
        if perm[i]>perm[pivot]:
            # swap
            perm[i],perm[pivot] = perm[pivot],perm[i]
            break
    
    # concat with reverse subset 
    return perm[:pivot+1]+ list(reversed(perm[pivot+1:]))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
    # X = [1,3,2]
    # print(next_permutation(X))
