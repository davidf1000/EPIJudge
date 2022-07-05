def paritycheck(x):
    sum = 0 
    while x:
        if x&1:
            sum+=1
        x = x >>1
    return not (sum%2==0)

print(paritycheck(0b01111))