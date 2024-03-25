class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq={}
        a=[]
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in freq:
            if freq[i]==2:
                a.append(i)
        return a

        
