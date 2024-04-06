class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        c=0
        for i in range(len(strs[0])):
            s=[]
            a=''
            for j in range(len(strs)):
                a+=strs[j][i]
            j=''.join(sorted(a))
            if j!=a:
                c+=1
        return c
