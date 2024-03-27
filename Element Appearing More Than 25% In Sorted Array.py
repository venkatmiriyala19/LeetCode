class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        a=len(arr)
        k=a*(25/100)
        for i in freq:
            if freq[i]>k:
                return i

        
