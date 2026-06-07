class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = 0     #for starting_value buying
        e = 1     # for ending_value selling
        maximum_profit = 0   # for initially 0

        while e < len(prices) :
            if prices[s] < prices[e] :
                profit = prices[e] - prices[s]
                maximum_profit = max(maximum_profit, profit)
            else :
                s = e 
            e = e + 1
        return maximum_profit