class Solution(object):
    def addDigits(self, num):
        def total(num):
            sum=0
            while(num>0):
                rem=num%10
                sum+=rem
                num=num//10
            if sum<10:
                return sum
            num=sum
            return total(num)
        return total(num)
        
        """
        :type num: int
        :rtype: int
        """
        
