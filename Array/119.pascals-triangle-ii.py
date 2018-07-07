class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        res = [self.func(rowIndex)/(self.func(i)*self.func(rowIndex-i)) for i in range(rowIndex+1)]
        
        return res
    

    def func(self, num):

        if num <= 1:
            return 1
        else:
            return num*self.func(num-1)


