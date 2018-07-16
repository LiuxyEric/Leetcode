class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_arr = [float("-inf")] * 3

        for num in nums:
            if num > max_arr[0]:
                max_arr[0], max_arr[1], max_arr[2] = num, max_arr[0], max_arr[1]
                count += 1
            elif num != max_arr[0] and num > max_arr[1]:
                max_arr[1], max_arr[2] = num, max_arr[1]
                count += 1
            elif num != max_arr[0] and num != max_arr[1] and num > max_arr[2]:
                max_arr[2] = num
                count += 1

        if count >= 3:
            return max_arr[2]
        else:
            return max_arr[0]
