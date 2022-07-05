from operator import is_
from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    # Create function to validate IP Address
    def is_valid(ip):
        # only 1 digit or >1 but first index can't be zero and total <=255
        return len(ip) == 1 or (ip[0] != '0' and int(ip) <= 255)
    # temp list for parts and result
    res, parts = [], [None]*4
    # loop first part from 1 to min(4,len), check if part is valid, if then proceed
    for i in range(1, min(4, len(s))):
        if is_valid(s[:i]):
            parts[0] = s[:i]
    # loop second part from 1 to min(4,len-first) , check if part is valid, if then proceed
            for j in range(1, min(4, len(s)-i)):
                if is_valid(s[i:i+j]):
                    parts[1] = s[i:i+j]
    # loop third&fourth part from 1 to min(4, len-second,first), if both valid append to result
                    for k in range(1, min(4, len(s)-i-j)):
                        parts[2], parts[3] = s[i+j:i+j+k], s[i+j+k:]
                        if is_valid(parts[2]) and is_valid(parts[3]):
                            res.append('.'.join(parts))
    return res


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))

    # T = '255255255255'
    # print(get_valid_ip_address(T))
