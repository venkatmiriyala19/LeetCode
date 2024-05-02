class Solution(object):
    def findMaxK(self, nums):
        a=set(nums)
        neg=[-1]
        for i in nums:
            if -i in a:
                neg.append(i)
        return max(neg)
        """
        :type nums: List[int]
        :rtype: int
        """
        
