class Solution(object):
    def isPowerOfFour(self, n):
        n=float(n)
        while n>=1:
            if n==1:
                return True
            n/=4
        return False
