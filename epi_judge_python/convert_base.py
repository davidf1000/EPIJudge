import string
from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # check if negative
    sign = '-' if num_as_string[0]=='-' else ''
    # convert from string to X with base b1 
    X = abs(int(num_as_string,b1))
    # convert from base 10 to base b2 
    res =[]
    while True:
        res.append(string.hexdigits[X%b2].upper())
        X//=b2
        if X==0:
            break
    return sign+ ''.join(reversed(res))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
    # print(convert_base('15',16,10))