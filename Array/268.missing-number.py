class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum1 = sum(nums)
        length = len(nums)
        sum2 = (length*(length-1)) / 2
        if sum1 >= sum2:
            sum2 = ((length+1)*length) / 2
            return sum2 - sum1
        else:
            return sum2 - sum1

