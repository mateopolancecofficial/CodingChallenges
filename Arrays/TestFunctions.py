from Arrays.RemoveDuplicatesFromSortedArray import RemoveDuplicatesSolution
from Arrays.BestTimeToBuyAndSellStock import BuySellStockSolution


def test_remove_duplicates_from_sorted_array():
    nums = [1, 1, 1, 2, 3, 3]
    solution = RemoveDuplicatesSolution()
    len = solution.removeDuplicates(nums)
    return len


def test_best_time_to_buy_and_sell_stocks():
    prices = [7, 1, 5, 3, 6, 4]
    solution = BuySellStockSolution()
    max_profit = solution.bestTimeToBuyAndSellStock(prices)
    return max_profit


