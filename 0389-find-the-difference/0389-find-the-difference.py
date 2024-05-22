class Solution(object):
    def findTheDifference(self, s, t):
        freq1={}
        freq2={}
        for i in s:
            if i in freq1:
                freq1[i]+=1
            else:
                freq1[i]=1
        for i in t:
            if i in freq2:
                freq2[i]+=1
            else:
                freq2[i]=1
        for i in freq2:
            if i not in freq1:
                return i
            if freq2[i]!=freq1[i]:
                return i
        
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        