class Solution(object):
    def canBeEqual(self, target, arr):
        target.sort()
        arr.sort()
        return arr==target
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        