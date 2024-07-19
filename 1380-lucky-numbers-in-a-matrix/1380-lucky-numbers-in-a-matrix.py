class Solution(object):
    def luckyNumbers (self, matrix):
        mini=[]
        col=[]
        for i in range(len(matrix[0])):
            col.append([])
        for i in range(len(matrix)):
            mini.append(min(matrix[i]))
            for j in range(len(matrix[0])):
                col[j].append(matrix[i][j])
        maxi=[]
        for i in col:
            maxi.append(max(i))
        s=set(mini)
        ans=[]
        for i in range(len(maxi)):
            if maxi[i] in s:
                ans.append(maxi[i])
        return ans

        
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        