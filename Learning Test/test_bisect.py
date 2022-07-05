from operator import indexOf
from time import time

def bisect(x,A):
    left,right = 0, len(A)-1
    while left<=right:
        print('before',left,right,x)
        mid = left//2 + right//2
        if A[mid] < x :
            left = mid + 1 
        elif A[mid] == x :
            return mid
        else:
            right = mid - 1
        print('after',left,mid,right)
    return -1

A = [0,1,2,3,4,5,6,7,8,9]
print([bisect(x,A) for x in range(10)])
