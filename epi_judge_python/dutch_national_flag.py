import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


"""
TODO - BASIC
* create 3 array 
* set pivot
* loop for i in range(len(list)):
*   if element < pivot:
*       append to list low 
*   elif elemnent == pivot:
*       append to list equal
*   else:
*       append to list high 
*   concat and assign to A

Time : O(n)
Space : O(n)

"""




def dutch_flag_partition_normal(pivot_index: int, A: List[int]) -> None:
    # TODO - you fill in here.
    low, equal, high = [],[],[]
    pivot = A[pivot_index]
    for item in A:
        if item<pivot:
            low.append(item)
        elif item==pivot:
            equal.append(item)
        else:
            high.append(item)
    A = low + equal + high
    print("Res: ",A)
    return

"""
TODO - space O(1) method

general idea : 
split into 4 section: low, equal, undefined,high
use pointer for low, equal ,and high 
while equal < high:
    if (item<pivot):
        swap item to index low, ++ low and equal
    elif (item==pivot):
        do nothing, ++ equal
    else (item>pivot):
        -- high, swap equal with high 

"""


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    low, equal, high = 0, 0, len(A)
    pivot = A[pivot_index]
    while equal<high:
        if(A[equal]<pivot):
            A[equal],A[low] = A[low],A[equal]
            low,equal = low + 1 , equal +1
        elif(A[equal] == pivot ):
            equal += 1
        else: # A[equal] > pivot
            high -=1
            A[equal],A[high] = A[high],A[equal]
    return
@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    # exit(
    #     generic_test.generic_test_main('dutch_national_flag.py',
    #                                    'dutch_national_flag.tsv',
    #                                    dutch_flag_partition_wrapper))
    X = [1,2,5,1,2,0,-3,-6,3]
    print("before: ",X)
    dutch_flag_partition(1,X)
    print("after: ",X)
