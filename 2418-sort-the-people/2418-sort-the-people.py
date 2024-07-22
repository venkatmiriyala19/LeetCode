class Solution(object):
    def sortPeople(self, names, heights):
        freq={}
        j=0
        for i in heights:
            freq[i]=names[j]
            j+=1
        heights.sort()
        res=[]
        for i in heights:
            res.append(freq[i])
        return res[::-1]


        

        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        