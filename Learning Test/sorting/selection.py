def selectionSort(A:list)->None:
    for i in range(len(A)-1):
        min_idx = i
        for j in range(i+1,len(A)):
            if A[j]<A[min_idx]: min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i] 


A = [1,6,3,2,-5,0]
selectionSort(A)
print(A)