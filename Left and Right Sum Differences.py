class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lsum=[0]
        rsum=[0]
        s=0
        for i in range(len(nums)-1):
            s=s+nums[i]
            lsum.append(s)
        s=0
        for i in range(1,len(nums)):
            s+=nums[-i]
            rsum.append(s)
        rsum.reverse()
        a=[]
        for i in range(len(nums)):
            a.append(abs(lsum[i]-rsum[i]))
        return a
