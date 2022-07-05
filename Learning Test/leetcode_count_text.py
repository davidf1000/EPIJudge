


def countTexts(pressedKeys:str) -> int:
    MOD = 1e9+7
    # base case 
    if len(pressedKeys)<=1: return 1
    # recursive
    sum, i, count = 0, 0, 1 
    # if 7,9, MAX_COUNT = 4, else 3
    if pressedKeys[i] == '7' or pressedKeys[i] == '9': max_count = 4 
    else: max_count = 3  
    # check number of duplicate
    while i+1<len(pressedKeys) and pressedKeys[i] == pressedKeys[i+1] and count<max_count: 
        count,i =count+ 1, i+1
    i+=1 # index sublist 
    for j in range(1,count+1): sum += countTexts(pressedKeys[j:]) % MOD
    return int(sum)





if __name__ == "__main__":
    print(countTexts('222222222222222222222222222222222222'))
