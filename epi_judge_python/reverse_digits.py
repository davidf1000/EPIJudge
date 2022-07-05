from test_framework import generic_test


def reverse(x: int) -> int:
    # TODO - you fill in here.
    res, remainder = 0 , abs(x)
    while remainder:
        # get right digit 
        right_digit = remainder % 10 
        # add digit * 10^i to res
        res = res*10 + right_digit
        # save the remainder
        remainder //=10
    # check return if x is negative 
    return -res if x<0 else res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
