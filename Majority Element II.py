class Solution(object):
    def majorityElement(self, nums):
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        a=len(nums)//3
        b=[]
        for i in freq:
            if freq[i]>a:
                b.append(i)
        return b
                
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
