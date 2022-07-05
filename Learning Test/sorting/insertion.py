def insertion_sort(A:list)->None:
    for i in range(1,len(A)):
        j = i-1
        while j>=0 and A[j]>A[j+1]:
            A[j],A[j+1] = A[j+1], A[j]
            j -= 1

def insertion_sort_optimized(A:list)->None:
    # Traverse through 1 to len(arr)
    for i in range(1, len(A)):
 
        key = A[i]
 
        # Move elements of A[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < A[j] :
                A[j + 1] = A[j]
                j -= 1
        A[j + 1] = key

                

A = [1,6,3,2,-5,0]
insertion_sort_optimized(A)
print(A)