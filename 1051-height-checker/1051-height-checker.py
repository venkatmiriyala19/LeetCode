class Solution(object):
    def heightChecker(self, heights):
        a=[]
        a[:]=heights
        count=0
        a.sort()
        for i in range(len(heights)):
            if heights[i]!=a[i]:
                count+=1
        return count
        """
        :type heights: List[int]
        :rtype: int
        """
        