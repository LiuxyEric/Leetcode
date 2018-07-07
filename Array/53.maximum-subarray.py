class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return []

        cumsum, maxsum = nums[0], nums[0]
        for num in nums[1:]:
            cumsum += num
            if cumsum <= num:
                cumsum = num
            if cumsum > maxsum:
                maxsum = cumsum

        return maxsum

            
            
