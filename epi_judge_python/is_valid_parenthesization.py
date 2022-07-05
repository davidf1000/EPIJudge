from re import L
from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    OPPOSITE:dict = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    stack =[]
    # loop over every chart
    # if in opposite, pop from stack, if match continue, else return false
    # if not in opposite, push to stack
    for item in s:
        if item in OPPOSITE:
            if len(stack) == 0:
                return False
            if OPPOSITE[item] != stack.pop():
                return False
        else:
            stack.append(item)
    return len(stack)==0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
