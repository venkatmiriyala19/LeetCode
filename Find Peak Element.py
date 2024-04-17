class Solution(object):
    def findPeakElement(self, nums):
        a=max(nums)
        return nums.index(a)
