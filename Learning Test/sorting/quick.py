def quick_sort(A:list)->None:
    def quick(A:list,s:int,e:int)->None:
        pivot = A[s]
        # base 
        if e-s == 1:
            A[e],A[s] = A[e],A[s] if A[e]<A[s] else A[s],A[e]
        if e-s == 0:
            return
        border = 0
        # rearrange
        temp1, temp2 = [],[]
        for i in range(s+1,e+1):
            if A[i]<pivot: temp1.append(A[i])
            else: temp2.append(A[])

        # recursive
        quick(A,s,border)
        quick(A,border+1,e)

            