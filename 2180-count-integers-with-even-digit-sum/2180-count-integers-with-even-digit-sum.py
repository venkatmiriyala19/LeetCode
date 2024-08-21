class Solution(object):
    def countEven(self, num):
        count=0
        for i in range(2,num+1):
            temp=0
            while(i!=0):
                rem=i%10
                temp+=rem
                i=i//10
            if temp%2==0:
                count+=1
        return count
        """
        :type num: int
        :rtype: int
        """
        