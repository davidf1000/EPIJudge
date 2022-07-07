from test_framework import generic_test

# n row
# m col

# base : x = 0 y = 0, ways = 1
# double for loop
# in (x,y), you can move up (x,y-1) or move left (x-1, y) to return to original position
# check DP_cache, if already there, just use that
# return DP_cache left bottom most


def number_of_ways(n: int, m: int) -> int:
    DP_cache = {(0, 0): 1}
    for x in range(n):
        for y in range(m):
            if(x != 0 or y != 0):
                last_left = DP_cache.get((x, y-1), 0)
                last_top = DP_cache.get((x-1, y), 0)
                DP_cache[(x, y)] = last_left + last_top
    return DP_cache[(n-1, m-1)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
