from typing import List

from test_framework import generic_test

# DP
# create DP cache for 13xlen(individual_scores) with 1 at final score 0
# loop i for len(individual)
# loop j for 12x (from 1 - 12)
# get DP from idx individual score else 0
# increment it with addition if new individual is added at hash[i][j-individual]
# store it in hash [i][j]
# return the last stage at the final score


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    DP = {}
    for individual_score_idx in range(len(individual_play_scores)):
        DP[individual_score_idx] = [1] + ([0] * final_score)
    for i in range(len(individual_play_scores)):
        for j in range(1, final_score+1):
            last_sum = DP.get(i-1, [0]*(final_score+1))[j]
            additional = DP.get(
                i)[j-individual_play_scores[i]] if j >= individual_play_scores[i] else 0
            DP[i][j] = last_sum + additional
    return DP[len(individual_play_scores)-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
