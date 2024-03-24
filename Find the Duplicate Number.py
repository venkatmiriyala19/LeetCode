class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            if i in freq:
                return i
            else:
                freq[i]=1
        
