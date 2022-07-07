import math
from typing import List

from test_framework import generic_test
import bintrees


class ABSqrt():
    def __init__(self, a, b) -> None:
        self.a, self.b = a, b
        self.val = a + b * math.sqrt(2)

    def __lt__(self, other) -> bool:
        return self.val < other.val

    def __eq__(self, other) -> bool:
        return self.val == other.val

# put the first iteration in the bintrees
# put result temp list
# while len temp is not k,
# pop smallest from bintrees and append to result
# put 2 candidate (+1 and +1(2)^1/2) inside bintrees


def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    binT = bintrees.RBTree([(ABSqrt(0, 0), None)])
    result = []
    while len(result) < k:
        min_val = binT.pop_min()[0]
        result.append(min_val.val)
        binT.insert(ABSqrt(min_val.a + 1, min_val.b), None)
        binT.insert(ABSqrt(min_val.a, min_val.b + 1), None)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
