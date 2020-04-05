#Problem Statement: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        total_profit=0
        while i<len(prices)-1:
            profit=prices[i+1]-prices[i]
            if profit>0:
                total_profit+=profit
            i+=1
        return total_profit
        
