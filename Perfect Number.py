class Solution(object):
    def checkPerfectNumber(self, num):
       
    
        if num == 1:
            return False
        n = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                n += i + num//i
        return n == num

        """
        :type num: int
        :rtype: bool
        """
        
