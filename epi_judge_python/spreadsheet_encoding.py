from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    n,sum = 0,0
    for item in reversed(col):
        sum+= (ord(item)-ord('A')+1)*(26**n)
        n+=1
    return sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
