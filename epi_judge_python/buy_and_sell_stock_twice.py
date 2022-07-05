from cmath import inf
from typing import List

from test_framework import generic_test




# def buy_and_sell_stock_twice(prices: List[float]) -> float:
#     # TODO - you fill in here.
#     # Create a temp array 
#     temp = [0]*len(prices)
#     # First step : fill temp with max profit (first buy)
#     max_profit = 0
#     min_price = inf
#     for i in range(len(prices)):
#         min_price=  min(min_price,prices[i])
#         max_profit = max(max_profit,prices[i]-min_price) 
#         temp[i] = max_profit
#     # Second step : add temp with second max profit (second buy sell)
#     max_profit = 0
#     max_value = 0
#     for i in reversed(range(len(prices))):
#         max_value = max(max_value,prices[i])
#         max_profit = max(max_profit,max_value-prices[i])
#         temp[i] += max_profit
#     return max(temp)

def buy_and_sell_stock_twice(prices: List[float]) -> float:
    buy1,sell1,buy2,sell2 = inf, 0, inf, 0 
    for i in range(len(prices)):
        buy1 = min(buy1,prices[i])
        sell1 = max(sell1,prices[i]-buy1)
        buy2 = min(buy2,prices[i]-sell1)
        sell2 = max(sell2,prices[i]-buy2)
    return sell2

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
