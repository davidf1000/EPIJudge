import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    # find m ^ t
    dupli_xor_miss = functools.reduce(lambda x, y: x ^ y, A+list(range(len(A))))
    # find k -> first 1 found in dupli_xor_miss
    k, res = 0, dupli_xor_miss
    while res & 1 != 1: res, k = res >> 1, k+1
    # function to check if element has bit 1 in loc k
    def check_if_match(element, k): return (element >> k) & 1 == 1
    # (m^t)^(x in A if bit nya ada)^(x in A_full if bitnya ada) = m or t
    m_or_t = functools.reduce(lambda x, y: x ^ y, [dupli_xor_miss]+[x for x in A if check_if_match(x, k)]+[
        x for x in list(range(len(A))) if check_if_match(x, k)
    ])
    # run m or t didalam A, jika ketemu then dupli, if not then missing
    if m_or_t in A: return DuplicateAndMissing(m_or_t, m_or_t ^ dupli_xor_miss)
    else: return DuplicateAndMissing(m_or_t ^ dupli_xor_miss, m_or_t)


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED,
                                  PropertyName.RESULT) else value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_missing_element.py',
                                       'find_missing_and_duplicate.tsv',
                                       find_duplicate_missing,
                                       res_printer=res_printer))
