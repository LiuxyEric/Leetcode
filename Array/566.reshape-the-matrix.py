class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row = len(nums)
        col = len(nums[0])
        if row*col != r*c or not nums:
            return nums
        
        matrix = [[0 for _ in range(c)] for _ in range(r)]

        count = 0
        for i in range(row):
            for j in range(col):
                matrix[count/c][count%c] = nums[i][j]
                count += 1

        return matrix
