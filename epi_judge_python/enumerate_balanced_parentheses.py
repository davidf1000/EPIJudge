from typing import List

from test_framework import generic_test, test_utils

# Base: n == num_pairs : append
# 3 scenario :
# 1. append () from left
# 2. append () from right
# 3. enclose with ()
# check if 1 and 2 diff, if yes do both, if no do only 1


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    if num_pairs == 0:
        return ['']
    if num_pairs == 1:
        return ['()']

    def generate(current_string: str, idx: int) -> None:
        # print(current_string, idx)
        if idx == num_pairs:
            result.append(current_string)
            return None
        case1, case2, case3 = '()' + current_string, current_string + \
            '()',  '('+current_string+')'
        generate(case3, idx+1)

        if case1 != case2:
            generate(case2, idx+1)
            generate(case1, idx+1)
        else:
            generate(case1, idx+1)

    result = []
    generate('()', 1)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
