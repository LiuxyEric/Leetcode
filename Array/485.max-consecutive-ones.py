class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_cnt = 0
        max_cnt = 0
        for num in nums:
            if num == 1:
                cur_cnt += 1
            else:
                if cur_cnt > max_cnt:
                    max_cnt = cur_cnt
                cur_cnt = 0
        if cur_cnt > max_cnt:
            max_cnt = cur_cnt

        return max_cnt
