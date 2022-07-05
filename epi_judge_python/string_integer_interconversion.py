from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    # check sign
    sign = '-' if x < 0 else ''
    x = abs(x)
    # add from right to left
    res = []
    while True:
        res.append(chr(ord('0')+x % 10))
        x //= 10
        if x == 0:
            break
    return sign + ''.join(reversed(res))


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    sign = -1 if s[0] == '-' else 1
    # loop for idx 1 - n  (reversed)
    # add number^idx to sum
    sum = 0
    n = 0
    for i in reversed(range(0, len(s))):
        if not s[i].isnumeric():
            break
        sum += int(s[i])*(10**n)
        n += 1
    return sign*sum


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))