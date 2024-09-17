class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a=s1.split(" ")
        b=s2.split(" ")
        freq={}
        c=[]
        for i in a:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in b:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in freq:
            if freq[i]==1:
                c.append(i)
        return c