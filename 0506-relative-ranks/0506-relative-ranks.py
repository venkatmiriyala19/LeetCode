class Solution(object):
    def findRelativeRanks(self, score):
        a=score[:]
        a.sort()
        a.reverse()
        freq={}
        count=1
        for i in a:
            freq[i]=count
            count+=1
        b=[]
        # print(score)
        for i in range(len(score)):
            # print(score[i])
            d=freq[score[i]]
            if d==1:
                b.append("Gold Medal")
            elif d==2:
                b.append("Silver Medal")
            elif d==3:
                b.append("Bronze Medal")
            else:
                b.append(str(d))
        return b
            
            
        """
        :type score: List[int]
        :rtype: List[str]
        """
        