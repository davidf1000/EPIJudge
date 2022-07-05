def closest_int_same_bit(x):
    # find k1, closest to LSB that is different from LSB 
    # loop for max bit -1 , check if the bit != right bit 
    BIT = 64 
    for i in range(BIT-1):
        if (x>>i)&1 != (x>>(i+1))&1:
            # swap the bit 
            bit_mask = (1<<i) | (1<<(i+1))
            x ^= bit_mask
        return (x)
    # raise error if input not valid 
    raise ValueError('all bit is 1 or 0 ! ')

    