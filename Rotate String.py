class Solution(object):
    def rotateString(self, s, goal):
        for i in range(len(s)):
            s=s[1:]+s[0]
            if s==goal:
                return True
        return False
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        
