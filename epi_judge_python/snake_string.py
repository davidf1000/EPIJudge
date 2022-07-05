from test_framework import generic_test


def snake_string(s: str) -> str:
    # TODO - you fill in here.
    res = []
    # looping first, 1 5 9 13 +4
    for i in range(1,len(s),4):
        res.append(s[i])
    # Looping second, 0, 2 ,4 ,6 ,8 +2 
    for i in range(0,len(s),2):
        res.append(s[i])
    # Looping third 3, 7, 11, +4
    for i in range(3,len(s),4):
        res.append(s[i])
    return ''.join(res)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
