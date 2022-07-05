def bubble_sort(A:list)->None:
    for i in range(len(A)):
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]

A = [1,6,3,2,-5,0]
bubble_sort(A)
print(A)