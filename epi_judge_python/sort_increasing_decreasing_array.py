import itertools
from typing import List
from sorted_arrays_merge import merge_sorted_arrays

from test_framework import generic_test


def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    if not A:
        return []
    # 1 is increasing
    # 0 is decreasing
    dir = 1 
    # loop for every element in array, if prev < current then current_dir ==1, else 0
    # if current dir == dir, keep appending to temp 
    # else : dir = current_dir, append temp to sorted_subarrays, empty temp, append element to temp 
    temp, sorted_subarrays = [A[0]],[]
    for i in range(1,len(A)):
        if A[i] > A[i-1]: current_dir =1 
        elif A[i] == A[i-1]: current_dir = dir 
        else: current_dir = 0
        if current_dir == dir:
            # still the same direction,append
            temp.append(A[i])
            #  if last index, just append the whole temp
            if i==(len(A)-1): 
                # print("LAST INDEX")
                sorted_subarrays.append(temp)
        else:
            # print('TEMP: ',temp,"DIRECTION",current_dir)
            dir = current_dir
            sorted_subarrays.append(temp)
            temp = [A[i]]
    # print(*sorted_subarrays)
    return sorted(itertools.chain(*sorted_subarrays))


if __name__ == '__main__':
    # print(sort_k_increasing_decreasing_array([1,2,3,-1,-2,-3,10,12,13,9,8]))
    # exit()
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
