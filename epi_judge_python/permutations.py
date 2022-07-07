from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    def compute_permutate(current_list : List[int], remaining: List[int])->None:
        if len(current_list) == len(A):
            result.append(list(A))
            return
        for item in (remaining):
            new_current, new_remaining = list(current_list), list(remaining)
            new_current.append(item)
            new_remaining.remove(item)
            compute_permutate(new_current, new_remaining)

    result = []
    compute_permutate([], list(A))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
