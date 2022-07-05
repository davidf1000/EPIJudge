


WORD_SIZE = 64

def parityCheck(x):
    n = WORD_SIZE
    while n>1:
        n//=2
        x ^= x>>n
        print(n)
    return x & 1

print(parityCheck(0b11011001001))

