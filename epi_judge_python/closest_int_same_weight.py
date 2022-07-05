from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    # find k1, closest to LSB that is different from LSB 
    # loop for max bit -1 , check if the bit != right bit 
    BIT = 64 
    for i in range(BIT-1):
        if (x>>i)&1 != (x>>(i+1))&1:
            # swap the bit 
            x ^= (1<<i) | (1<<(i+1))
            return (x)
    # raise error if input not valid 
    return 0
    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
