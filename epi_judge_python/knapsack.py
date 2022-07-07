import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))

# DP_cache, create len(items) * (capacity+1)
# loop for items, then loop for  capacity (1->cap)
# value for that pos = max(didnt_use, use)
# didnt_use = get from previous items cache
# use = weight for that item + cache(idx - weight)
# return DP_cache[-1][-1]


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    DP = [[0] * (capacity+1) for _ in range(len(items))]
    for item_idx in range(len(items)):
        for cap in range(1, capacity+1):
            weight = items[item_idx].weight
            value = items[item_idx].value
            if weight <= cap:
                pass
                DP[item_idx][cap] = max(
                    DP[item_idx-1][cap], (value + DP[item_idx-1][cap-weight]))
            else:
                DP[item_idx][cap] = DP[item_idx-1][cap]
    return DP[-1][-1]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    # items = [Item(5, 60), Item(3, 50), Item(4, 70), Item(2, 30)]
    # print(optimum_subject_to_capacity(items, 5))
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
