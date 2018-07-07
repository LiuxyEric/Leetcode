class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxpro = 0

        if len(prices) <= 1:
            return maxpro

        for i in range(1, len(prices)):
            maxpro += max(0, prices[i] - prices[i-1])

        return maxpro
