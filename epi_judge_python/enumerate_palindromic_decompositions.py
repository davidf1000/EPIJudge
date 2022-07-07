from typing import List

from test_framework import generic_test

# recursive
# base condition : idx == len(text), append
# loop for i in range(idx, len(text)):
# check if substring is palindrome, if yes T(curr_strings + [substring], idx+len(substring))


def palindrome_decompositions(text: str) -> List[List[str]]:
    def palindrome(current_strings: List[str], idx: int) -> None:
        if idx == len(text) :
            result.append(current_strings)
            return None
        for i in range(idx+1, len(text)+1):
            substring = text[idx:i]
            if substring == substring[::-1]:
                palindrome(current_strings + [substring], idx + len(substring))

    result = []
    palindrome([], 0)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'enumerate_palindromic_decompositions.py',
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
