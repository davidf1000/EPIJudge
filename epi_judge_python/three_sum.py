from typing import List

from test_framework import generic_test

# loop for each item, i
# A[i] + A[j] + A[k] == t
# A[j] + A[k] == t - A[i]
# do above loop by setting j,k = 0, len
# if less, move left ->
# if more, move  <- right


def has_three_sum(A: List[int], t: int) -> bool:
    A.sort()
    for i in range(len(A)):
        j, k = 0, len(A)-1
        while j <= k:
            if A[j] + A[k] == t - A[i]:
                return True
            elif A[j] + A[k] < t - A[i]:
                j += 1
            else:  # more
                k -= 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
