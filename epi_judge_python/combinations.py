from typing import List

from test_framework import generic_test, test_utils


def combinations(n: int, k: int) -> List[List[int]]:
    input_set = list(range(1, n+1))
    def generate(current_list: List[int], idx: int) -> None:
        if idx == len(input_set):
            result.append(current_list)
            return None
        # 1. include
        generate(list(current_list + [input_set[idx]]), idx+1)
        # 2. not include
        generate(list(current_list), idx+1)
    result = []
    generate([], 0)
    return [x for x in result if (len(x) == k)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
