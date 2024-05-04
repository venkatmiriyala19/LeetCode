class Solution(object):
    def uniqueOccurrences(self, arr):
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        s=set()
        for i in freq:
            if freq[i] in s:
                return False
            s.add(freq[i])
        return True
        """
        :type arr: List[int]
        :rtype: bool
        """
        
