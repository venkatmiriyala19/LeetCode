class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a=set(nums)
        l=list(a)
        if len(a)>2:
            l.sort()
            return l[-3]
        return l[-1]
        

        