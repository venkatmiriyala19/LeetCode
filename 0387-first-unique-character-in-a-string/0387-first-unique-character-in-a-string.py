class Solution(object):
    def firstUniqChar(self, s):
        s1=''
        for i in range(len(s)-1):
            x=s1+s[i+1:]
            if s[i] not in x:
                return i
            s1+=s[i]
        if s[-1] not in s1:
            return len(s)-1
        return -1
        """
        :type s: str
        :rtype: int
        """
        