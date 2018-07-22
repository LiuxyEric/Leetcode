class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(M)
        col = len(M[0])
        def getGray(M, i, j):
            
            total, count = 0, 0
            for m in range(-1,2):
                for n in range(-1, 2):
                    ii = i + m
                    jj = j + n
                    if 0 <= ii < row and 0 <= jj < col:
                        total += M[ii][jj]
                        count += 1
            return int(total / count)
        
        result = [[0 for _ in range(col)] for _ in range(row)] 
        for i in range(row):
            for j in range(col):
                result[i][j] = getGray(M, i, j)

        return result
