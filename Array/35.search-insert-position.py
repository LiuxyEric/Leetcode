class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first, last = 0, len(nums) - 1
        while first <= last:
            mid = first + (last - first) / 2
            if nums[mid] >= target:
                last = mid - 1
            else:
                first = mid + 1

        return first

