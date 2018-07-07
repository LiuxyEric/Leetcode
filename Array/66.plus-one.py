class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        arr = digits[::-1]
        length = len(digits) - 1

        for i, value in enumerate(arr):
            if value < 9:
                arr[i] += 1
                return arr[::-1]
            elif value == 9:
                arr[i] = 0
                if i == length:
                    arr = arr + [1]
        return arr[::-1]




        

