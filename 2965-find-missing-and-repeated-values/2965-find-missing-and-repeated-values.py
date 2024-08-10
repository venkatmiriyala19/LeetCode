class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        s=set()
        res=[]
        for i in grid:
            for j in i:
                if j in s:
                    res.append(j)
                else:
                    s.add(j)
        for i in range(1,len(s)+2):
            if i not in s:
                res.append(i)
                break
        return res
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        