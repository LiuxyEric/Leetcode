class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        prev = nums[0]
        less_count = 0
        more_count = 0
        for num in nums[1:]:
            if num < prev:
                prev = num
            else:
                if count > 1:
                    

