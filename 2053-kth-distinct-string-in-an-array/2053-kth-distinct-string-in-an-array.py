class Solution(object):
    def kthDistinct(self, arr, k):
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in arr:
            if freq[i]==1 and k>1:
                k-=1
            elif freq[i]==1 and k==1:
                return i
        return ""
                
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        