from re import X
from test_framework import generic_test

# gcd(x, y) = gcd(y, x % y)
# basis : if (y==0) -> return x
# return gcd(y, x%y)

def gcd(x: int, y: int) -> int:
    if (y==0): return x
    return gcd(y,x % y)

if __name__ == '__main__':
    exit(generic_test.generic_test_main('euclidean_gcd.py', 'gcd.tsv', gcd))
