




def remove_all_adjacent_duplicate(s:str,k:int)->str:
    stack = []
    for i,c in enumerate(s):
        peek = stack[-1] if stack else None
        if peek and c == peek[0]:
            count = peek[1] +1  
            stack.append((c,count))
            if count >=k:
                for _ in range(k):
                    stack.pop()
        else: stack.append((c,1))
    return ''.join([x[0] for x in stack])






if __name__ == '__main__':
    # s = 'abcd'
    # print(remove_all_adjacent_duplicate(s,2))
    # s = 'deeedbbcccbdaa'
    # print(remove_all_adjacent_duplicate(s,3))
    s= "yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy"
    print(remove_all_adjacent_duplicate(s,4))
    # s= "pbbcggttciiippooaais"
    # print(remove_all_adjacent_duplicate(s,2))
