from typing import List

from test_framework import generic_test, test_utils

# recursive
# base : n == len(input set): append list of set into result
# 1. choose to include the number and recusive idx++
# 2. choose not to include the number and recusive idx++


def generate_power_set(input_set: List[int]) -> List[List[int]]:
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
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
