class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_element = float('inf')
        profit = float('-inf')
        for num in prices:
            min_element = min(min_element, num)
            profit = max(profit, num - min_element)
        return profit