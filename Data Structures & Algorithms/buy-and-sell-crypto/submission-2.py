class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        for i in range(len(prices) - 1, 0 , -1):
            buy = max(i-1, 0) # buying index
            while prices[i] > prices[buy] and buy >= 0:
                maximum = max(maximum, prices[i] - prices[buy])
                buy -= 1
        return maximum

            