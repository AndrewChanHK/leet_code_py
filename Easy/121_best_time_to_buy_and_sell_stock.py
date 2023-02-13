# 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        gain, low = 0, prices[0]
        for e in prices:
            gain = max(gain, e-low)
            low = min(low, e)
        return gain
