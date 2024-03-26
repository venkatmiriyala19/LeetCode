class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        a=max(nums)
        s=set(nums)
        for i in range(2,a):
            if i not in s:
                return i
        return a+1
        
