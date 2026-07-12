class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        l = 0
        r = 1
        maxprofit = 0
        while r<len(prices):
            if prices[l]>=prices[r]:
                l=r
                r+=1
            elif prices[r]>prices[l]:
                maxprofit = max(maxprofit, prices[r]-prices[l])
                r+=1
        return maxprofit        