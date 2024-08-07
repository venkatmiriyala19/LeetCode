class Solution(object):
    def restoreString(self, s, indices):
        s1=''
        res=[]
        for j in range(len(indices)):
            res.append(0)
        j=0
        for i in indices:
            res[i]=s[j]
            j+=1
        # print(res)
        return "".join(res)

        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """