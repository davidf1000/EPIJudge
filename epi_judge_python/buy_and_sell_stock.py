from cmath import inf
from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    profit_max = 0
    min_price_so_far = inf
    # loop for i in range prices:
        # check compare for the current low 
        # calculate the now profit = current - currentlow  
        # if profit now > profit max -> profit max = profit now 
    for i in range(len(prices)):
        min_price_so_far = prices[i] if prices[i]< min_price_so_far else min_price_so_far
        current_profit = prices[i] - min_price_so_far
        if prices[i]-min_price_so_far > profit_max:
            profit_max = current_profit
    return profit_max


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
