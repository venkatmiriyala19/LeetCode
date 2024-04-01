class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a=0
        b=0
        if target not in nums:
            return [-1,-1]
        for i in range(len(nums)):
            if nums[i]==target:
                a=i
                break
        c=a
        for i in range(len(nums[a+1:])):
            c=c+1
            if nums[c]==target:
                b=c              
        if b==0:
            return [a,a]
        return [a,b]
        
