from test_framework import generic_test


# recursive
# base: maximum_step > top
# for i in range(1, maximumstep+1):
# check i <= maximumstep
# if yes, recursive for (top - i, maximumstep)

def number_of_ways_to_top(top: int, maximum_step: int) -> int:
    # print()
    # print(top, maximum_step)
    if top == 0:
        return 1
    if top < 0:
        return 0
    count = 0
    for step in range(1, maximum_step+1):
        if step <= top:
            count += number_of_ways_to_top(top - step, maximum_step)
    return count


def number_of_ways_to_top_dp(top: int, maximum_step: int) -> int:
    DP = {}

    def recursive(top: int):
        if top == 0:
            return 1
        count = 0
        # check if already in cache or not
        if top in DP:
            return DP[top]
        # not in DP, count manually then store it into DP
        for step in range(1, maximum_step + 1):
            if step <= top:
                count += recursive(top-step)
        DP[top] = count
        return DP[top]

    return recursive(top)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_staircase.py',
                                       'number_of_traversals_staircase.tsv',
                                       number_of_ways_to_top_dp))
