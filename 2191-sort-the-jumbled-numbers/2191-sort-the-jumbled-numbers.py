class Solution(object):
    def sortJumbled(self, mapping, nums):
        res=[]
        for i in nums:
            a=str(i)
            s=''
            for j in a:
                s+=str(mapping[int(j)])
            res.append((i,int(s)))
        res.sort(key=lambda x: x[1])
        return [num for num, _ in res] 
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        