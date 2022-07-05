import bisect
import itertools


def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    try:
        return list(itertools.chain(*matrix)).index(target) is not None
    except:
        return False

print(searchMatrix([[1,2,3],[4,5,6]],100))