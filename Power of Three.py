class Solution(object):
    def isPowerOfThree(self, n):
        if n<=0:
            return False
        logvalue=log10(n)/log10(3)
        return logvalue==int(logvalue)
        """
        :type n: int
        :rtype: bool
        """
        
