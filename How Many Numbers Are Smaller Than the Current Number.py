class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        kol=nums[:]
        kol.sort()
        freq={}
        for i in range(len(kol)):
            if kol[i] not in freq:
                freq[kol[i]]=i
        kol=[]
        
        for i in range(len(nums)):
            kol.append(freq[nums[i]])
        return kol

        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
