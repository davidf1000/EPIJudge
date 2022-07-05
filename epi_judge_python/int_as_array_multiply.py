from typing import List

from test_framework import generic_test

"""
create list with len A*B
check sign 
make first digit abs 
for i in Reverse(len A):
    sum = 0
    for j in Reverse(len B):
        sum = A[i]*B[i]
        ovf = sum // 10 
        A[i+j+1] = sum % 10
        A[i+j] += ovf

remove leading zero 


"""
def multiply(num1: List[int], num2: List[int]) -> List[int]:
    # TODO - you fill in here.
    result = [0]*(len(num1)+len(num2))
    sign = -1 if num1[0]*num2[0]<0 else 1
    num1[0],num2[0] = abs(num1[0]),abs(num2[0])
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10      
    # Remove leading zero 
    result = result[next((i for i,x in enumerate(result) if x!=0),len(result)):] or [0]
    print(result)
    return [sign*result[0]] + result[1:]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
    # multiply([1,2],[1,0])