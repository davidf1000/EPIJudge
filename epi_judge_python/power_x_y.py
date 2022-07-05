from test_framework import generic_test


def power(x: float, y: int) -> float:
    # TODO - you fill in here.
    res, pow = 1, y 
    if y < 0 :
        pow , x = -pow, 1/x 
    while pow:
        # base 
        if pow & 1 : 
            res *= x
        x , pow = x*x, pow>>1
    return res


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
