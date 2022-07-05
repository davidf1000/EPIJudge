from typing import List

from test_framework import generic_test

"""
1. Brute force: 
[x for x in enumerate(A) if (i==0 or A[i-1] != a) and a in B]
O(mn) time complexity 

2. bisect approach 
same with brute force, except use bisect to search if A[i] in B:
O(mlogn) time 

3. sliding window approach 
temp = []
i, j for A and B pointer
while i or j in bounds:
    if A[i] = B[j]:
        dup = A[j]
        temp.append(dup)
        shift A and B pointer to right until not dup
    i++, j++
O(m+n) time complexity
"""

def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    if not A or not B:
        return []
    temp = []
    i,j = 0,0    
    while i<len(A) and j<len(B):
        print(temp)
        print(i,j,A[i],B[j])
        if A[i] == B[j]:
            dup = A[i]
            temp.append(dup)
        # shift until the next unique item
        dupA, dupB = A[i], B[j] 
        if dupA<=dupB:
            while i<len(A) and A[i] == dupA:
                i+=1
        if dupB<=dupA:
            while j<len(B) and B[j] == dupB:
                j+=1
        
    return temp


if __name__ == '__main__':
    print(intersect_two_sorted_arrays([1,1,1,1,2],[2,3,4]))
    # # exit()
    # exit(
    #     generic_test.generic_test_main('intersect_sorted_arrays.py',
    #                                    'intersect_sorted_arrays.tsv',
    #                                    intersect_two_sorted_arrays))
