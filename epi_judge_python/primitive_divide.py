from test_framework import generic_test


def divide(x: int, y: int) -> int:
    # TODO - you fill in here.
    # find biggest y2^k <= x
    # then x-=y2^k and sum+=y2^k
    sum =0
    for i in range(64-1,-1,-1):
        num = y << i
        if num <= x:
            x -= num
            sum += 1<<i           
    return sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
