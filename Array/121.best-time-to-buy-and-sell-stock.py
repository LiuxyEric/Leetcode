class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        start, cur,  maxpro = prices[0], 0, 0
        for num in prices[1:]:
            if num <= start:
                start = num
            else:
                cur = num - start
                if cur > maxpro:
                    maxpro = cur
        return maxpro
                
