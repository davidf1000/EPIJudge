from typing import List

from test_framework import generic_test


def minimum_total_waiting_time(service_times: List[int]) -> int:
    service_times.sort()
    sum = 0
    prev = 0
    for idx in range(1, len(service_times)):
        curr_wait_time = service_times[idx-1] + prev
        prev = curr_wait_time
        sum += curr_wait_time
    return sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_waiting_time.py',
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
