class Solution(object):
    def deleteGreatestValue(self, grid):
        for i in range(len(grid)):
            grid[i].sort()
        summer=0
        for i in range(1,len(grid[0])+1):
            maxi=0
            for j in range(len(grid)):
                maxi=max(maxi,grid[j][-i])
            summer+=maxi
        return summer
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        