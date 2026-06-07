class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prc = prices[0]
        max_profit = 0
        for i in prices:
            if i < min_prc:
                min_prc = i
            else:
                max_profit = max(max_profit, i - min_prc)
        return max_profit