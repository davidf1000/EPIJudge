from cmath import inf
import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    if not A:
        return 0
    max_simul = -inf
    endpoint = [(x.start, True) for x in A] + [(x.finish, False) for x in A]
    endpoint.sort(key=lambda x: (x[0], not x[1]))
    sum = 0
    for item in endpoint:
        if item[1]:
            sum += 1
            max_simul = max(max_simul, sum)
        else:
            sum -= 1
    return max_simul


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
