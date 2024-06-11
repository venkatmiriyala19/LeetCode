class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        a=[]
        b=set(arr2)
        s=set(arr1)
        for i in arr1:
            if i not in b:
                a.append(i)
        freq={}
        for i in arr1:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        c=[]
        for i in arr2:
            for j in range(freq[i]):
                c.append(i)
        a.sort()
        c=c+a
        return c
                
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        