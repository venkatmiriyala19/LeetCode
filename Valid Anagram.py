class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        freq={}
        freq2={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in t:
            if i in freq2:
                freq2[i]+=1
            else:
                freq2[i]=1
        for i in freq:
            if i not in freq2:
                return False
            if freq[i]!=freq2[i]:
                return False
        return True
       

        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
