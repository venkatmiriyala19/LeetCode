class Solution(object):
    def threeConsecutiveOdds(self, arr):
        c=0
        for i in arr:
            if i%2!=0:
                c+=1
            if c==3:
                return True
            if i%2==0:
                c=0
        return False
        """
        :type arr: List[int]
        :rtype: bool
        """
        
