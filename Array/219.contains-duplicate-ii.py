class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                prev_idx = dic[nums[i]]
                if i - prev_idx <= k:
                    return True
                else:
                    dic[nums[i]] = i
            else:
                dic[nums[i]] = i
        return False

