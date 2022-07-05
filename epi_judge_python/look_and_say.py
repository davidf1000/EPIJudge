from test_framework import generic_test


def look_and_say(n: int) -> str:
    if n==0:
        return ''
    res = ['1']
    # sort the strings 
    # while loop until i==len-1 
    # get the first seen number, do while loop until the number changed
    # add number concat with the counter
    for i in range(n-1):
        str_list = list(res[i])
        idx = 0
        temp = []
        while idx<len(str_list):
            num = str_list[idx]
            count=0
            while idx<len(str_list) and str_list[idx]==num:
                count+=1
                idx+=1
            temp.extend([str(count),str(num)])
        res.append(''.join(temp))
    return res[n-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
    # print(look_and_say(4))