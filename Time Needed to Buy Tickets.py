class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        time=0
        while(tickets[k]!=0):
            for i in range(len(tickets)):
                if tickets[i]>0:
                    tickets[i]-=1
                    time+=1
                if tickets[k]==0:
                    break
        return time
            
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        
