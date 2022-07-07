import collections
from typing import List

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))

# sort
# pair the n biggest to n lowest


def optimum_task_assignment(task_durations: List[int]) -> List[PairedTasks]:
    task_durations.sort()
    res = []
    for i in range(len(task_durations)//2):
        res.append(PairedTasks(task_durations[i], task_durations[~i]))
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('task_pairing.py', 'task_pairing.tsv',
                                       optimum_task_assignment))
