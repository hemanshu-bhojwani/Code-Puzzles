# Leetcode 121: Best Time to Buy and Sell Stock

# Initial Solution
# Time Complexity: O(n^2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
        return max_profit
