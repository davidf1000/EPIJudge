from list_node import ListNode

def print_num(n:int)->int:
    # base
    if n==0:
        return 0 
    num = 1 + print_num(n-1)
    print(num)
    return num

print_num(10)

# time complexity O(n)
# space complexity O(n)
def find_pair(l:list,sum:int)->(int,int):
    m = {}
    for item in l:
        if item not in m:
            m[sum-item] = item
        else: # item in m
            return (m[item],item)
    return None

L = [0, -1, 2, 0, 1]
res = find_pair(L,0)
print("not found" if not res else res) 
    
def reverse_string(string:str)->str:
    temp = list(string)
    for i in range(len(temp)//2):
        temp[i], temp[~i] = temp[~i], temp[i]
    
    return ''.join(temp)
print(reverse_string("123"))