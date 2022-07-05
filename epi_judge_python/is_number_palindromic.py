import math
from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    # TODO - you fill in here.
    if(x<=0):
        return x==0
    # loop for n//2 +1
    n = math.floor(math.log10(x))+1
    print("n",n) 
    for i in range (n//2):
        # extract msb and lsb 
        # check if true 
        n = math.floor(math.log10(x))+1
        lsb = x%(10)
        msb = x//(10**(n-1))
        print(lsb,msb)
        if(lsb!=msb):
            return False        
        x -= lsb
        x-= msb*(10**(n-1))
        x//= 10
        print(x)
        if(x<0):
            return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
    # print(is_palindrome_number(10011))
