class Solution(object):
    def repeatedNTimes(self, nums):
        freq=set()
        for i in nums:
            if i in freq:
                return i
            else:
                freq.add(i)
        
        """
        :type nums: List[int]
        :rtype: int
        """
        