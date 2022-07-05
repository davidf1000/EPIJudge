from cmath import inf
from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    # loop for each map, ++ every dist
    # loop for each string, add to hashmap if not in hashmap
    # if already in hashmap, save distance inside second map, then reset
    # return max distance from second map, return 0 if empty 
    dist_counter, nearest = {} , -1
    for i,string in enumerate(paragraph):
        if string in dist_counter: nearest = min(inf if nearest==-1 else nearest,i-dist_counter[string])
        dist_counter[string] = i
    return nearest

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
