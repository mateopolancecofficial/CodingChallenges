"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
"""
from typing import List


class BuySellStockSolution:
    def bestTimeToBuyAndSellStock(self, prices: List[int]) -> int:
        """
        :param prices: List[int]
        :return: int - max profit
        """

        min_value = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):

            if prices[i] < min_value:
                min_value = prices[i]

            elif prices[i] > min_value:
                max_profit += prices[i] - min_value
                min_value = prices[i]

        return max_profit
