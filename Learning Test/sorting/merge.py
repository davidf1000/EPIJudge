def merge_sort(A:list)->list:
    list_size = len(A)
    print(A)
    # base condition
    if list_size == 1:
        return [A[0]]
    if list_size == 2:
        return [A[0],A[1]] if A[0]<A[1] else [A[1],A[0]]
    
    # recursive
    L1 = merge_sort(A[:list_size//2 + 1])
    L2 = merge_sort(A[list_size//2 + 1 : list_size])
    
    temp = [None]*list_size
    # merging 
    current, left, right = 0, 0, 0
    left_max, right_max = len(L1)-1, len(L2)-1
    while left<=left_max or right <= right_max:
        if left <=left_max and right <= right_max:
            if L1[left] < L2[right]:
                temp[current] = L1[left]
                left +=1
            else:
                temp[current] = L2[right]
                right +=1
        elif left<=left_max and right >right_max:
            temp[current] = L1[left]
            left +=1
        else:
            temp[current] = L2[right]
            right +=1
        current +=1
    
    return temp


A = [1,6,3,2,-5,0]
print(merge_sort(A))