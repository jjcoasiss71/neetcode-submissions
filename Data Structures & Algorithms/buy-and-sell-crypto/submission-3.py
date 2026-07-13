class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        minPrice = prices[0]
        for i in prices[1:]:
            if i < minPrice:
                minPrice = i
            else:
                maximum = max(maximum, i-minPrice)
        return maximum

            