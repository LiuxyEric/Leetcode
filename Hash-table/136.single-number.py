class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = nums[0]
        for i in nums[1:]:
            first = first ^ i
        return first
