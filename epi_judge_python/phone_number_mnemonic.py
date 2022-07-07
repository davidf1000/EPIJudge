from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:
    # TODO - you fill in here.
    # Create hashmap on the possible combination
    MAP = {
        '0': ['0'],
        '1': ['1'],
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'Q', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y', 'Z']
    }
    # Create a recursion function with input of list and start index

    def generate_combination(L: list, temp: list, s: int) -> None:
        # idx == len, append temp into res
        if s == len(L):
            res.append(''.join(temp))
            return
        for j in MAP[L[s]]:
            print(j)
            generate_combination(L, temp+[j], s+1)
    res = []
    generate_combination(list(phone_number), [], 0)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))

    # T = '123'
    # print(phone_mnemonic(T))
