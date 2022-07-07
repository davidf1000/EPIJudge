from typing import List

from test_framework import generic_test

# recursively
# base -> start == len(A): return 1
# max_count = 0
# loop for start+1 until end of sentence
# if value greater equal, max_count = max(max_count, 1 + recursive(start))


def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    def recursive(start: int) -> int:
        if start == len(A):
            return 1
        max_count = 0
        for i in range(start+1, len(A)):
            if i >= A[start]:
                max_count = max(max_count, recursive(i + 1))
        return max_count
    return recursive(-1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_nondecreasing_subsequence.py',
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
