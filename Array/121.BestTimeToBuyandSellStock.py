class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxx = 0

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                profit = prices[i] - buy
                maxx = max(maxx, profit)


        return maxx



