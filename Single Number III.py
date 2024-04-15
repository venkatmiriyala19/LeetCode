class Solution(object):
    def singleNumber(self, nums):
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        a=[]
        for i in freq:
            if freq[i]==1:
                a.append(i)
        return a
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
