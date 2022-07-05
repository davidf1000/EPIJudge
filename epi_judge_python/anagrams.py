from typing import List

from test_framework import generic_test, test_utils


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    hashmap = {}
    for s in dictionary:
        sorted_string = ''.join(list(sorted(s)))
        if sorted_string in hashmap: 
            hashmap[sorted_string].append(s)
        else:
            hashmap[sorted_string] = [s]
    return [x for x in hashmap.values() if len(x)>=2]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
