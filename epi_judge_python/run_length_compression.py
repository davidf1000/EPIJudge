from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    # for loop dengan gap 2
    idx = 0
    res = []
    while idx < len(s)-1:
        # find number,
        num = ''
        while s[idx].isnumeric():
            num += s[idx]
            idx += 1
        num = int(num)
        char = s[idx]
        # simpan count and char
        res.extend([char]*num)
        idx += 1
    return ''.join(res)


def encoding(s: str) -> str:
    # create curr_idx
    res = []
    curr_idx = 0
    while curr_idx < len(s):
        # get number, then while element != num and <len, keep counting
        count = 0
        char = s[curr_idx]
        while curr_idx < len(s) and s[curr_idx] == char:
            count += 1
            curr_idx += 1
        # assign count and number to the res
        res.append(str(count))
        res.append(str(char))
    return ''.join(res)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
    # T = '3e4f2e'
    # print(decoding(T))
    # E =decoding('T')
    # print(encoding(E))
