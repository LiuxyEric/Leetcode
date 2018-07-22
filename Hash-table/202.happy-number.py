class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lookup = {}
        while n != 1 and n not in lookup:
            lookup[n] = True
            n = sum([x**2 for x in map(int, str(n))])
        return n == 1

