class Solution(object):
    def findDisappearedNumbers1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        return list(set(range(1, len(nums) + 1)) - set(nums))
    

    def findDisappearedNumbers(self, nums):

        for i in range(len(nums)):
            if nums[abs(nums[i]) -1] > 0:
                nums[abs(nums[i]) - 1] *= -1

        result = []

        for i in range(len(nums)):

            if nums[i] > 0:
                result.append(i+1)
            else:
                nums[i] *= -1

        return result
