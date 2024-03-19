class Solution(object):
    def maximizeSum(self, nums, k):
        a=max(nums)
        s=0
        for i in range(k):
            s+=a
            a+=1
        return s
