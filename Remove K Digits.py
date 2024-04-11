class Solution(object):
    def removeKdigits(self, num, k):
        stack=[]
        for i in range(len(num)):
            while stack and num[i]<stack[-1] and k>0:
                stack.pop()
                k-=1
            stack.append(num[i])
        stack=stack[:-k] if k>0 else stack
        result=''.join(stack).lstrip('0')
        return result if result else '0'

        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
