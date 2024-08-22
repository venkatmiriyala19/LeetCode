class Solution(object):
    def findComplement(self, num):
        a=bin(num)
        a=a[2:]
        s=''
        for i in a:
            if i=='0':
                s+='1'
            else:
                s+='0'
        return int(s,2)
        """
        :type num: int
        :rtype: int
        """
        