class Solution(object):
    def defangIPaddr(self, address):
        s=''
        for i in address:
            if i=='.':
                s+='['+'.'+']'
                continue
            s+=i
        return s
        """
        :type address: str
        :rtype: str
        """
        
