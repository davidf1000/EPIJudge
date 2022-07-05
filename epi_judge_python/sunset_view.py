from typing import Iterator, List

from test_framework import generic_test


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    # sequence is from east to west 
    # W <---X E
    # Loop for each item
    # if build > peek(), while loop to pop() stack until build<peek() then append
    stack = []
    for i in range(len(sequence)):
        if len(stack)==0: # first building, always can be seen
            stack.append(i)
            continue
        if sequence[i] >= sequence[stack[-1]]:
            while sequence[i] >= sequence[stack[-1]]:
                stack.pop()
                if len(stack)==0:
                    break
        stack.append(i)
    return list(reversed(stack))


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    # print(examine_buildings_with_sunset([6, 9, 3, 9, 5, 16, 9, 13]))
    # exit()
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
