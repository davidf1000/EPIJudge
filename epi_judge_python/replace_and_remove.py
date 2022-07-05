from asyncore import write
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    # creatw write index, and count a 
    write_idx, count_a = 0,0
    # loop the array, if b dont write, else write it, if a count it 
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            count_a += 1

    curr_idx = write_idx -1 
    write_idx += count_a -1 
    final_size = write_idx + 1 
    while curr_idx>=0:
        # if not a, replace like ussual
        if s[curr_idx] !='a' :
            s[write_idx] = s[curr_idx]
            write_idx-=1
        else:
            # if a, write 2 d backward then increment2x write idx
            s[write_idx] = s[write_idx-1] = 'd'
            write_idx-=2
        curr_idx-=1 
    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
