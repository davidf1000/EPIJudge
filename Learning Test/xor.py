import functools
from time import time


def find_unique(A:list):
    for i in range(len(A)):
        cond = True
        for j in range(len(A)):
            if j == i: continue
            if A[i] == A[j]:
                cond = False
                break
        if cond: return A[i]
    return None
        


testcase = [
    [1,1,2,2,3,3,4,4,5],
    [1,3,2,4,4,2,1],
    [-1,-4,-3,-3,-1,-5,-5,-4],
    [1]
]
t = time()
for test in testcase:
    print(test)
    print(find_unique(test))
print('finished in ',int(1000000*(time()-t))/1000,'ms')