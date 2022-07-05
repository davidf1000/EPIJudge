from test_framework import generic_test

def add_num(a,b):
    c = 0
    while b:
        c = a & b 
        a = a ^ b 
        b = c << 1 
    return a
def multiply(x: int, y: int) -> int:
    # TODO - you fill in here.
    print(x,y)
    res = 0 
    while x:
        lsb = x & 1
        if lsb:
            res = add_num(res,y)
        x >>=1
        y <<=1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
