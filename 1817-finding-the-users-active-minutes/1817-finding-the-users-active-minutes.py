class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        freq={}
        for i in range(len(logs)):
            freq[logs[i][0]]=set()
        for i in range(len(logs)):
            freq[logs[i][0]].add(logs[i][1])
        a=[]
        for i in range(k):
            a.append(0)
        for i in freq:
            a[len(freq[i])-1]+=1
        return a

        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        