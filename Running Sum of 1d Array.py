class Solution(object):
    def runningSum(self, nums):
        s=0
        l=[]
        for i in nums:
            s+=i
            l.append(s)
        return l
