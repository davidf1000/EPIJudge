from test_framework import generic_test


def test_collatz_conjecture(n: int) -> bool:
    # 1 2 3 4 5 6 
    # 1 : 1 
    # 2 : 2 1 
    # 3 : 10 5 16 8 4 2 1
    # 4 : 2 1 
    # 5 : 16 8 4 2 1
    # 6 : 3 16 8 4 2 1
    temp = set()
    max = 1
    def is_collatz_true(num:int)->bool:
        temp.add(num)
        while num!=1:
            is_even = num%2==0
            if num < max:
                if num in temp or is_even: return True
            if is_even: num = num >> 1
            else: num = num*3 + 1
        return True

    return all([is_collatz_true(i) for i in range(1,n+1)])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('collatz_checker.py',
                                       'collatz_checker.tsv',
                                       test_collatz_conjecture))
