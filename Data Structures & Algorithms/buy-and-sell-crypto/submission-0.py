class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float("inf")
        maxx = float("-inf")
        for i in range(0, len(prices)):
            if prices[i]< minprice :
                minprice = prices[i]
            prof = prices[i]- minprice
            maxx = max(maxx,prof)
        return  maxx