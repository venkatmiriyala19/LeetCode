class Solution(object):
    def rowAndMaximumOnes(self, mat):
        a=[]
        c=0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j]==1:
                    c+=1
            a.append(c)
            c=0
        b=max(a)
        d=a.index(b)
        return [d,b]
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        
