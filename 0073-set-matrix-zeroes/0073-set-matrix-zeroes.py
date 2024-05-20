class Solution(object):
    def setZeroes(self, matrix):
        r=set()
        c=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    r.add(i)
                    c.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in r or j in c:
                    matrix[i][j]=0
        return matrix
        

        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        