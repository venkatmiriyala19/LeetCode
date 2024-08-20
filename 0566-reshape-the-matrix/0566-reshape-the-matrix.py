class Solution(object):
    def matrixReshape(self, mat, r, c):
        flatten=[]
        for i in mat:
            for j in i:
                flatten.append(j)
        if len(mat)*len(mat[0])!=r*c:
            return mat
        res=[]
        a=0
        for i in range(r):
            temp=[]
            for j in range(c):
                temp.append(flatten[a])
                a+=1
            res.append(temp)
        return res

        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        